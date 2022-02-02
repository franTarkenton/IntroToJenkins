""" In this demo:

a) Create a virtualenv
b) install dependencies
c) run script using virtualenv


# source data:
ag/cap:
    * https://catalogue.data.gov.bc.ca/dataset/agriculture-capability-mapping
    * http://www.env.gov.bc.ca/esd/distdata/ecosystems/Soil_Data/AgricultureCapability/AgCap_Map_GDB_20150923.zip

thlb:
   * https://catalogue.data.gov.bc.ca/dataset/provincial-timber-harvesting-land-base-thlb-by-timber-supply-area-tsa-
   * https://www.for.gov.bc.ca/ftp/HTS/external/!publish/THLB/tsa_thlb.zip

"""
import os.path
import subprocess
import requests
import constants
import logging
import zipfile
import archook

archook.get_arcpy(pro=True)
import arcpy

LOGGER = logging.getLogger()

class DownloadData:

    def __init__(self, datadir, dryRun=False):
        self.datadir = datadir
        self.dryRun = dryRun
        if not os.path.exists(datadir):
            LOGGER.info(f"creating the directory: {datadir}")
            os.makedirs(datadir)

    def download(self):
        fname = os.path.join(self.datadir, 'agcap.zip')
        if not os.path.exists(fname):
            LOGGER.debug("downloading the ag data")
            url = constants.AG_DATA_URL
            r = requests.get(url)
            open(fname , 'wb').write(r.content)
            LOGGER.debug("extracting the ag data")
            with zipfile.ZipFile(fname, 'r') as zip_ref:
                zip_ref.extractall(self.datadir)

        fname2 = os.path.join(self.datadir, 'soil.zip')
        if not os.path.exists(fname2):
            LOGGER.debug("download the soil data")
            url = constants.SOIL_URL
            r = requests.get(url)
            open(fname2 , 'wb').write(r.content)
            LOGGER.debug("extracting the soil data")
            with zipfile.ZipFile(fname2, 'r') as zip_ref:
                zip_ref.extractall(self.datadir)

    def createResultant(self):
        outDir = os.path.join(self.datadir, constants.OUTPUT_GDB)
        if not os.path.exists(outDir):
            LOGGER.debug("creating the output FGDB")
            arcpy.management.CreateFileGDB(self.datadir, constants.OUTPUT_GDB)
        resultant = os.path.join(self.datadir, constants.OUTPUT_GDB, 'resultant')
        if not arcpy.Exists(resultant):
            fcList = self.getFeatureClasses()
            LOGGER.info("creating a resultant...")
            if not self.dryRun:
                arcpy.analysis.Union(fcList, resultant)

    def getFeatureClasses(self):
        contents = os.listdir(self.datadir)
        gdbs = []
        for f in contents:
            LOGGER.debug(f"f is: {f}")
            if os.path.splitext(f)[1].lower() == '.gdb':
                gdbs.append(f)

        fcList = []
        for gdb in gdbs:
            curdir = os.path.join(self.datadir, gdb)
            arcpy.env.workspace = curdir
            fcs = arcpy.ListFeatureClasses("*")
            for fc in fcs:
                fcPath = os.path.normpath(os.path.join(curdir, fc))
                fcList.append(fcPath)
        listString = '\n'.join(fcList)
        LOGGER.info(f"feature classes: {listString}")
        return fcList

if __name__ == '__main__':

    loglevel = logging.DEBUG
    # logging setup
    LOGGER.setLevel(loglevel)
    hndlr = logging.StreamHandler()
    formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(message)s"
    )
    hndlr.setFormatter(formatter)
    LOGGER.addHandler(hndlr)
    LOGGER.debug("first test message")

    dl = DownloadData(constants.DATADIR, dryRun=True)
    dl.download()
    dl.createResultant()
