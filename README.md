# pair_style cosine/squared - A LAMMPS pair style with extended reach

This project contains an implementation of a LAMMPS _pair\_style_ that has a cosine-squared attractive part with adaptable width. Optionally it can also have a repulsive part equal to that of a Lennard-Jones potential (also known as the Weeks-Chandler-Andersen potential, but without the shift).

This potential was first proposed, described and used by Cooke, Kremer & Deserno ([Tunable generic model for fluid bilayer membranes, 2005](https://doi.org/10.1103/PhysRevE.72.011506)) as the tail-bead interaction of a three-bead lipid membrane model. In the article the full interaction potential between tail beads is actually the superposition of the WCA repulsive and the cosine-squared attractive part, which in this pair style can be achieved through the optional `wca` parameter.

An implementation of just the cosine-squared, attractive part for LAMMPS can be found in [this repository by Peter Wirnsberger](https://github.com/pw359/membrane), which also served as the basis for this implementation.

### Installing

To install the pair style just copy-paste it into the **src** directory of your LAMMPS and rebuild the whole LAMMPS (using make).

It is has been tested on the `16Mar2018` stable release and the master branch as of 20th of August, 2018.

### Usage

The name of the interaction in LAMMPS is `cosine/squared`, and the signature of the `pair_style` command is the follwing:
```
pair_style cosine/squared <cutoff> (wca yes/no)
```
where _cutoff_ is the global cutoff for all particle type pairs and _wca_ is an optional parameter which, if chosen, makes the pair style include a repulsive Weeks-Chandler-Andersen part to the interaction.

The signature of the `pair_coeff` command is:
```
pair_coeff <type_1> <type_2> <eps> <sigma> <cutoff>
```
where _type\_1_ and _type\_2_ are particle types, _eps_ is the interaction strength (depth), _sigma_ is the distance at which the minimum is achieved, and _cutoff_ (optional) is the distance at which the potential vanishes (if different from the global cutoff).

An example LAMMPS input script using the pair style, along with a tool to plot the interaction force and potential, can be found in the **test** directory.

## TODO

* add documentation (LaTeX with equations & graphs for potential & force) + LAMMPS style doc?
