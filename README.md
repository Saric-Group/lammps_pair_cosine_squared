# lj/cos_sq - A Lennard-Jones-like LAMMPS pair style with extended (cosine-squared) reach

This project contains an implementation of a LAMMPS _pair\_style_ that has a repulsive part (and minimum) equal to that of a Lennard-Jones potential (also known as the Weeks-Chandler-Andersen potential, but without the shift) which is smoothly joined to a cosine-squared attractive part with adaptable width.

This potential was first proposed, described and used by Cooke, Kremer & Deserno ([Tunable generic model for fluid bilayer membranes, 2005](https://doi.org/10.1103/PhysRevE.72.011506)) as the tail-bead interaction of a three-bead lipid membrane model. In the article, however, the two parts of the potential (the WCA repulsive and the cosine-squared attractive part) are given separately, while here they are implemented as a single interaction potential.

An implementation of just the cosine-squared, attractive part for LAMMPS can be found in [this repository by Peter Wirnsberger](https://github.com/pw359/membrane), which also served as the basis for this implementation.

### Installing

To install the pair style just copy-paste it into the **src** directory of your LAMMPS and rebuild it (using make).

It is has been tested on the `16Mar2018` stable release and the master branch as of 20th of August, 2018.

### Usage

The name of the interaction in LAMMPS is `lj/cos_sq`, and the signature of the `pair_style` command is the same as for most pair styles (like `lj/cut`), namely:
```
pair_style lj/cos_sq <cutoff>
```
where _cutoff_ is the global cutoff for all particle type pairs.

The signature of the `pair_coeff` command is:
```
pair_coeff <type_1> <type_2> <eps> <delta> <cutoff>
```
where _type\_1_ and _type\_2_ are particle types, _eps_ is the interaction strength (depth), _delta_ is the distance at which the minimum is achieved, and _cutoff_ (optional) is the distance at which the potential vanishes (if different from the global cutoff).

An example LAMMPS input script using the pair style, along with a tool to plot the interaction force and potential, can be found in the **test** directory.

## TODO

* add documentation (LaTeX with equations & graphs for potential & force) + LAMMPS style doc?
