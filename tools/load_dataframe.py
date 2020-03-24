import pandas as pd

sample_names = '''rearrangement amino_acid frame_type rearrangement_type
templates reads frequency productive_frequency cdr3_length v_family
v_gene v_allele d_family d_gene d_allele j_family j_gene j_allele
v_deletions d5_deletions d3_deletions j_deletions n2_insertions
n1_insertions v_index n1_index n2_index d_index j_index v_family_ties
v_gene_ties v_allele_ties d_family_ties d_gene_ties d_allele_ties
j_family_ties j_gene_ties j_allele_ties sequence_tags v_shm_count
v_shm_indexes antibody sample_name species locus product_subtype
kit_pool total_templates productive_templates outofframe_templates
stop_templates dj_templates
total_rearrangements productive_rearrangements outofframe_rearrangements
stop_rearrangements dj_rearrangements total_reads
total_productive_reads total_outofframe_reads total_stop_reads
total_dj_reads productive_clonality productive_entropy
sample_clonality sample_entropy sample_amount_ng
sample_cells_mass_estimate fraction_productive_of_cells_mass_estimate
sample_cells fraction_productive_of_cells max_productive_frequency
max_frequency counting_method primer_set release_date sample_tags
fraction_productive order_name kit_id total_t_cells'''.split()

def load_dataframe(filename):
    return pd.read_csv(filename,
                       sep='\t',
                       header=None,
                       names=sample_names,
                       index_col=False,
                       na_values=['unresolved'])

cdr3_v_j = ['amino_acid', 'j_family', 'j_gene', 'j_allele', 'v_family', 'v_gene', 'v_allele']
