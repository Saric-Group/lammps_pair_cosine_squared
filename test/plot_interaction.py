# encoding: utf-8
'''
A standalone program that plots the potential and force from a LAMMPS pair_write output.

Created on 18 Aug 2018

@author: Eugen Rožić
'''
import argparse
parser = argparse.ArgumentParser(description='''
        An application that plots the potential and force from a LAMMPS pair_write output file''',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument('data_file', help='path to the pair_write output data file, e.g. "interaction.dat"')
parser.add_argument('-s', '--save', default=None, type=str, help='saves the figure to the given file path/name')
args = parser.parse_args()

import matplotlib.pyplot as plt

with open(args.data_file, 'r') as data_file:
    data_file.readline()
    data_file.readline()
    name = data_file.readline().strip()
    N = int(data_file.readline().split()[1])
    data_file.readline()
    rs = [0.0]*N
    Es = [0.0]*N
    Fs = [0.0]*N
    min_E = 0.0
    for i in range(N):
        parts = data_file.readline().split()
        rs[i] = float(parts[1])
        Es[i] = float(parts[2])
        Fs[i] = float(parts[3])
        if Es[i] < min_E:
            min_E = Es[i]

axis_font = {'size':12}
fig = plt.figure('LAMMPS lj/cos_sq interaction force & potential', figsize=(10,8))

plt.plot(rs, Es, 'k-', linewidth=1.5, label='potential')
plt.plot(rs, Fs, 'k--', linewidth=1.5, label='force')

#--------------------------------------------------
#import numpy as np
#
#def lj(r, sigma, eps=1.0):
#    return eps*((sigma/r)**12 - 2*(sigma/r)**6)
#
#def lj_force(r, sigma, eps=1.0):
#    return eps*12*((sigma/r)**12 - (sigma/r)**6)/r
#
#plt.plot(rs, lj(np.array(rs), 1.5), 'r--', linewidth=1.0, label='V_LJ')
#plt.plot(rs, lj_force(np.array(rs), 1.5), 'r-.', linewidth=1.0, label='F_LJ')
#--------------------------------------------------

plt.legend(loc='lower right')
plt.axis(xmin = rs[0], xmax = rs[-1], ymin = 1.05*min_E, ymax = -1.05*min_E)
plt.xlabel(r'$r$', **axis_font)

if args.save:
    fig.savefig(args.save, format='pdf', dpi=1000)

plt.show()
