"""
This is for encode and decode data so that the data can store by Solidity in smart contracts.
"""


def encode(pp):
    # result = pp.age_quantile + "#" + pp.hemoglobin + "#" + pp.platelets + "#" + pp.MPV + "#" + pp.RBC + \
    #          "#" + pp.lymphocytes + "#" + pp.MCHC + "#" + pp.leukocytes + "#" + pp.basophils + "#" + pp.MCH + \
    #          "#" + pp.eosinophils + "#" + pp.MCV + "#" + pp.monocytes + "#" + pp.RDW + \
    #          "#" + str(pp.detection_coronaviridae) + "#" + str(pp.detection_orthomyxoviridae) + \
    #          "#" + str(pp.detection_paramyxoviridae) + "#" + str(pp.detection_picornaviridae) + \
    #          "#" + str(pp.detection_pneumoviridae)
    list = []
    for fea in pp.features:
        list.append(fea)
    separator = "#"
    list_str = map(str, list)
    result = separator.join(list_str)
    #print(result)
    return result


def decode(aggregation):
    result = aggregation.split('#')
    return result
