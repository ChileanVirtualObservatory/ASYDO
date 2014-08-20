# Create several cubes in parallel, using random parameters
from multiprocessing import Pool
from Universe import *
from IMCM import *
from DataBase import *
import math
import random
import numpy as np
import sys
import time
import matplotlib.pyplot as plt

SPEED_OF_LIGHT = 299792458.0
KILO = 1000

def rget(val):
   if isinstance(val,tuple):
      return random.uniform(val[0],val[1])
   else:
      return val

class CubeFactory:
   def  __init__(self,log,dbpath,x_pos=0.0,y_pos=0.0,f_pos=300000,spa_pix=5,spe_pix=100,fov=500,bw=100000,rvel=(150,1000),temp=300,semiaxis=(10,300),fwhm=(10,50),angle=(0,math.pi),rot=0,curtosis=0):
      self.log=log
      self.rvel=rvel
      self.dbpath=dbpath
      self.x_pos=x_pos
      self.y_pos=y_pos
      self.f_pos=f_pos
      self.spa_pix=spa_pix
      self.spe_pix=spe_pix
      self.bw=bw
      self.fov=fov
      self.temp=temp
      self.semiaxis=semiaxis
      self.fwhm=fwhm
      self.rot=rot
      self.angle=angle
      self.curtosis=curtosis
      self.force_list=list()
      self.ban_list=list()

   def forceMolecule(self,name):
      self.force_list.append(name)

   def banMolecule(self,name):
      self.ban_list.append(name)

   def unitaryGen(self,n):
      print "Generating cube", n
      db=DataBase(self.dbpath)
      db.connect()
      univ=Universe(log)
      xpos=rget(self.x_pos)
      ypos=rget(self.y_pos)
      univ.createSource('AutoGenCube-'+str(n),xpos,ypos)
      fpos=rget(self.f_pos)
      bw=rget(self.bw)
      rv=rget(self.rvel)
      lf=(fpos - bw/2.0)*math.sqrt((1 + rv*KILO/SPEED_OF_LIGHT)/(1 - rv*KILO/SPEED_OF_LIGHT))
      uf=(fpos + bw/2.0)
      chList=db.getMoleculeList(lf,uf)
      temp=rget(self.temp)
      print chList
      # HERE Random selection of molecules
      for chName in chList:
         molist=db.getSpeciesList(chName[0],lf,uf)
         for mol in molist:
            s_x=rget(self.semiaxis)
            s_y=rget(self.semiaxis)
            angle=rget(self.angle)
            rot=rget(self.rot)
            fw=rget(self.fwhm)
            curt=rget(self.curtosis)
            model=IMCM(self.log,mol[0],temp,('normal',s_x,s_y,angle),('skew',fw,curt),('linear',angle,rot))
            model.setRadialVelocity(rv)
            univ.addComponent('AutoGenCube-'+str(n),model)
      fov=rget(self.fov)
      bw=rget(self.bw)
      cspec=CubeSpec(xpos,ypos,fpos,fov/self.spa_pix,fov,bw/self.spe_pix,bw)
      cube=univ.genCube('AutoGenCube-'+str(n),cspec)
      db.disconnect()
      return cube

   def parallelGen(self,samples,nproc):
      
      p = Pool(nproc)
      result=p.map(gen_cube,range(samples))
      return result


      #info = np.asarray(result)
      #np.save('exp1.npy', info)
log=sys.stdout
factory=CubeFactory(log,'ASYDO')
cube=factory.unitaryGen(1)
