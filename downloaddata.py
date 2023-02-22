import pandas as pd
import numpy as np
import os
import sys
import datetime

if not os.path.exists(sys.argv[1]):
 os.mkdir(sys.argv[1])

# Input year to download year.

year= sys.argv[1]

mainlink = "https://noaa-gefs-retrospective.s3.amazonaws.com/GEFSv12/reforecast/"+sys.argv[1]+"/"



# Generate dates.
d1 = datetime.date(int(year), 1, 1)
d2 = datetime.date(int(year), 12, 31)

days = [d1 + datetime.timedelta(days=x) for x in range((d2-d1).days + 1)]

alldates = []
for day in days:
    alldates.append(day.strftime('%Y%m%d')+"00")
    
print(alldates[0])


# define 5 sets

allsets = ["c00","p01","p02","p03","p04"]


# Define days.
days = ["Days%3A1-10","Days%3A10-16"]
#days = ["Days%3A10-16"]

#days = ["Days:1-10","Days:10-16"]


# List of all the possible variables.

allvariables = [
'acpcp_sfc',
'apcp_sfc',
'cape_sfc',
'cin_sfc',
'dlwrf_sfc',
'dswrf_sfc',
'gflux_sfc',
'gust_sfc',
'hgt_ceiling',
'hgt_hybr',
'hgt_pres',
'hgt_sfc',
'hlcy_hgt',
'lhtfl_sfc',
'ncpcp_sfc',
'pbl_hgt',
'pres_hybr',
'pres_msl',
'pres_pvor',
'pres_sfc',
'pvort_isen',
'pwat_eatm',
'rh_hybr',
'sfcr_sfc',
'shtfl_sfc',
'soilw_bgrnd',
'spfh_2m',
'spfh_pres',
'tcdc_eatm',
'tmax_2m',
'tmin_2m',
'tmp_2m',
'tmp_hybr',
'tmp_pres',
'tmp_pvor',
'tmp_sfc',
'tozne_eatm',
'tsoil_bgrnd',
'uflx_sfc',
'ugrd_hgt',
'ugrd_hybr',
'ugrd_pres',
'ugrd_pvor',
'ulwrf_sfc',
'ulwrf_tatm',
'uswrf_sfc',
'vflx_sfc',
'vgrd_hgt',
'vgrd_hybr',
'vgrd_pres',
'vgrd_pvor',
'vvel_pres',
'watr_sfc',
'weasd_sfc']


# Define the variables to be extracted 
# https://noaa-gefs-retrospective.s3.amazonaws.com/index.html#GEFSv12/reforecast/2000/2000010100/c00/Days:1-10/
# Visit above link


allvariables = [
'acpcp_sfc']


# Dates for which data is to be extracted.

for date in alldates[0:10]:
 
 if not os.path.exists(sys.argv[1]+os.sep+date):
  os.mkdir(sys.argv[1]+os.sep+date)
  
 for set in allsets:

  if not os.path.exists(sys.argv[1]+os.sep+date+"/"+set):
   os.mkdir(sys.argv[1]+os.sep+date+"/"+set)
   
  for d in days:
   
   if not os.path.exists(sys.argv[1]+os.sep+date+"/"+set+"/"+d):
    os.mkdir(sys.argv[1]+os.sep+date+"/"+set+"/"+d)
    
   for v in allvariables: 
     filename1 = mainlink+date +"/"+set+"/"+d+ "/"+ v+"_"+ date+"_"+set+"."+"grib2"
     filename2 = mainlink+date +"/"+set+"/"+d+ "/"+ v+"_"+ date+"_"+set+"."+"grib2.idx"
     destination = sys.argv[1]+os.sep+date+"/"+set +"/"+d
     
     print(filename1)
     print(filename2)
     
     os.system("wget "+filename1+" -P "+destination)
     os.system("wget "+filename2+" -P "+destination)
     

     
     
     
  
  



exit(0)




































