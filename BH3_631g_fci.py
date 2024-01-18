file_string = "BH3_631g_fci"
mol_str = """
B   0.000000000000  0.000000000000 -0.000000014895
H   -0.000000000000  0.000000000000  1.193230299466
H   1.033367824431  0.000000000000 -0.596615068378
H   -1.033367824431 -0.000000000000 -0.596615068378
symmetry c1
"""
options_dict = {'basis': '6-31g',
         'scf_type': 'pk',
         'e_convergence': 1e-11,
         'd_convergence': 1e-11
         }
cavity_dict = {
    'omega_value' : 0.,
    'lambda_vector' : np.array([0, 0, 0.0]),
    'ci_level' : 'fci',
    'davidson_roots' : 250,
    'number_of_photons' : 0,
    'davidson_threshold' : 1e-8,
    'photon_number_basis' : True,
    'canonical_mos' : True,
    'coherent_state_basis' : False
}
test_pf = PFHamiltonianGenerator(
    mol_str,
    options_dict,
    cavity_dict
)
# save eigenvalues and dipole elements to npy files 
#C_string = file_string + "_Eigenvectors"
E_string = file_string + "_Energies"
Mu_string = file_string + "_Dipoles"
#np.save(C_string, test_pf.CIvecs)
np.save(E_string, test_pf.CIeigs)
np.save(Mu_string, test_pf.dipole_array)