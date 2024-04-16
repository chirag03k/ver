
import sys, os

import config
from dindex_store.discovery_index import load_dindex
from aurum_api.algebra import AurumAPI
from qbe_module.query_by_example import ExampleColumn, QueryByExample
from qbe_module.join_graph_search import JoinGraphType

cnf = {setting: getattr(config, setting) for setting in dir(config)
       if setting.islower() and len(setting) > 2 and setting[:2] != "__"}

dindex = load_dindex(cnf)
print("Loading DIndex...OK")

api = AurumAPI(dindex)
print("created aurum api")

# QBE interface
qbe = QueryByExample(api)

example_columns = [
    ExampleColumn(attr='customer_id', examples=['234', '5933']),
    ExampleColumn(attr='wealth_segment', examples=['High Net Worth', 'Mass Customer']),
    ExampleColumn(attr='product_id', examples=['88', '17']),
    ExampleColumn(attr='list_price', examples=['323.13', '23.21']),
]

candidate_list = qbe.find_candidate_columns(example_columns, cluster_prune=True)
cand_groups, tbl_cols = qbe.find_candidate_groups(candidate_list)
join_graphs = qbe.find_join_graphs_for_cand_groups(cand_groups)
print('done')

print(f"number of join graphs: {len(join_graphs)}")
with open('join_graph_ground_truth_2.csv', 'a+') as f:
    join_graphs_strs = map(lambda j: j.to_str(), filter(lambda x: x.type != JoinGraphType.NO_JOIN, join_graphs))
    for line in f:
        if line.replace(",", " JOIN ") in join_graphs_strs:
            join_graphs_strs.remove(line)
    add = "\n".join(map(lambda x: x.replace(" JOIN ", ","), join_graphs_strs))
    print(list(join_graphs_strs))
    print(add)
    f.write(add)