#!/usr/bin/python
import os, os.path
from sys import platform
if os.name == 'nt' or platform == 'win32':
    os.chdir(os.path.dirname(__file__))
import ast
import pickle
from copy import deepcopy


def readlines_until_empty_line(file, mark=""):
    count_x=0
    reactions = []
    while True:
        line = file.readline()
        
        if (line == "" and count_x==0):
            return None
        one_reaction = line.rstrip()
        if (line == "\n" and count_x != 0):
            return reactions
        reactions.append(one_reaction)
        count_x+=1

def read_pathway_txt(pathways_file):
    pathways_list=[]
    while True:
        one_pathway_text_list=readlines_until_empty_line(pathways_file, mark="")
        one_pathway_list=[]
        if one_pathway_text_list==None:
            break
        for one_reaction_str in one_pathway_text_list:
            one_reaction=ast.literal_eval(one_reaction_str)

            #if one_reaction[2]==('CH@3,C,CH2,CH2,CH2,CH2,NH2,NH2,OH,O~100001100100100000001100000001000000020000000',):
                #one_reaction=tuple([one_reaction[0],one_reaction[1],('CH,C,CH2,CH2,CH2,CH2,NH2,NH2,OH,O~100001100100100000001100000001000000020000000',),one_reaction[3]])
            
            one_pathway_list.append(one_reaction)
        pathways_list.append(one_pathway_list)
    return pathways_list

def find_new_tb_sub(one_pathway,tb_sub,current_lv,distance):

    tb_sub_copy=copy(tb_sub)
    new_tb_sub=[]
    for reaction in one_pathway:
        for cmpd_tb_sub in tb_sub:
            if reaction[0]==current_lv-distance and cmpd_tb_sub in reaction[1] and len(reaction[1])==1:
                if cmpd_tb_sub in tb_sub_copy:
                    tb_sub_copy.remove(cmpd_tb_sub)
                    for rctt in reaction[2]:
                        new_tb_sub.append(rctt)
                    


    if tb_sub_copy!=[]:
        return []
    else:
        return new_tb_sub


def replace_node(node_name):
    if node_name=="O=C(O)C(=O)CC(O)C(O)C(O)COP(=O)(O)O":
        return "DAHP"
    if node_name=="O=P(O)(O)OCC1OC(O)(CO)C(O)C1O":
        return "F6P"
    if node_name=="C=C(OP(=O)(O)O)C(=O)O":
        return "PEP"
    if node_name=="O=CC(O)C(O)COP(=O)(O)O":
        return "E4P"
    if node_name=="O=C(O)C(CO)OP(=O)(O)O":
        return "2PG"
    if node_name=="O=C(O)C(O)COP(=O)(O)O":
        return "3PG"
    if node_name=="C(C(C=O)O)OP(=O)(O)O":
        return "GA3P"
    if node_name=="O=C(CO)C(O)C(O)COP(=O)(O)O":
        return "X5P"
    if node_name=="O=P(O)(O)OCC1OC(O)(COP(=O)(O)O)C(O)C1O":
        return "F16bP"
    if node_name=="O=C(O)C(O)COP(=O)(O)O":
        return "DHAP"
    return node_name



def main2():
    #print pathways_list

            #                [
            #                    [
            #                        [ (-1, ('target_cmpd'), ('reactant_bwd_lv_1_cmpd', ...), 'enzyme') ],
            #                        [ ], [ ], ... [ ]
            #                    ],
            #
            #                    [
            #                        [ (-1, ('target_cmpd'), ('reactant_bwd_lv_1_cmpd', ...), 'enzyme'), 
            #                            (-2, ('product_bwd_lv_1_cmpd'), ('reactant_bwd_lv_2_cmpd', ...), 'enzyme'), 
            #                            (-2, ('product_bwd_lv_1_cmpd'), ('reactant_bwd_lv_2_cmpd', ...), 'enzyme'), ( ), ... ( )  ], [ ], ... [ ],
            #                        [ (-2, ('target_cmpd'), ('reactant_bwd_lv_2_cmpd', ...), 'enzyme') ], [ ], ... [ ]
            #                    ],
            #
            #                    [
            #                        [ (-1, ('target_cmpd'), ('reactant_bwd_lv_1_cmpd', ...), 'enzyme'), 
            #                            (-2, ('product_bwd_lv_1_cmpd'), ('reactant_bwd_lv_2_cmpd', ...), 'enzyme'),
            #                            (-2, ('product_bwd_lv_1_cmpd'), ('reactant_bwd_lv_2_cmpd', ...), 'enzyme'), ( ), ... ( ), 
            #                                (-3, ('product_bwd_lv_2_cmpd'), ('reactant_bwd_lv_3_cmpd', ...), 'enzyme'), 
            #                                (-3, ('product_bwd_lv_2_cmpd'), ('reactant_bwd_lv_3_cmpd', ...), 'enzyme'), ( ), ... ( ) ], [ ], ... [ ],
            #                        [ (-2, ('target_cmpd'), ('reactant_bwd_lv_2_cmpd', ...), 'enzyme'),
            #                            (-3, ('product_bwd_lv_2_cmpd'), ('reactant_bwd_lv_3_cmpd', ...), 'enzyme'), 
            #                            (-3, ('product_bwd_lv_2_cmpd'), ('reactant_bwd_lv_3_cmpd', ...), 'enzyme'), ( ), ... ( ) ], [ ], ... [ ],
            #                        [ (-3, ('target_cmpd'), ('reactant_bwd_lv_3_cmpd', ...), 'enzyme') ], [ ], ... [ ]
            #                    ],
            #                    ......
            #                ]



    nodes_list=[] # actually 
    node_value_dict=dict([])
    link_set_list=[]
    link_set_s_t_list=[]


    pathways_file=open("pathways_F6P3.txt")
    pathways_list=read_pathway_txt(pathways_file)
    print pathways_list
    for one_pathway in pathways_list:
        for i in one_pathway[-1][2]:
            if replace_node(i) not in nodes_list:
                nodes_list.append(replace_node(i))
                node_value_dict[replace_node(i)]=0
        for one_rxn in one_pathway:
            for i in one_rxn[1]:
                if replace_node(i) not in nodes_list:
                    nodes_list.append(replace_node(i))
                    node_value_dict[replace_node(i)]=one_rxn[0]
                else:
                    node_value_dict[replace_node(i)]=min(one_rxn[0],node_value_dict[replace_node(i)])
            one_rxn_1=[]
            one_rxn_2=[]
            for i in one_rxn[1]:
                one_rxn_1.append(replace_node(i))
            for i in one_rxn[2]:
                one_rxn_2.append(replace_node(i))
            if set(one_rxn_1+one_rxn_2) not in link_set_list:
                link_set_list.append(set(one_rxn_1+one_rxn_2))
                link_set_s_t_list.append([set(one_rxn_1),set(one_rxn_2)])

    print node_value_dict
    print nodes_list
    print link_set_list
    print link_set_s_t_list
    print "first step done"
    #--------------------------------------------------#
    
    pickle_in1=open("../zz_test_savings/networks_bwd_F6P","rb")
    networks_bwd=pickle.load(pickle_in1)
    pickle_in1.close()
    pickle_in2=open("../zz_test_savings/networks_fwd_F6P","rb")
    networks_fwd=pickle.load(pickle_in2)
    pickle_in2.close()
    print len(networks_bwd)
    #--------------------------------------------------#
    main_nodes_list=deepcopy(nodes_list)
    count_x=0
    for one_pathway in networks_fwd:
        count_x+=1
        if count_x>15:
            break
        for i in one_pathway[-1][2]:
            if replace_node(i) not in nodes_list:
                nodes_list.append(replace_node(i))
            if replace_node(i) not in main_nodes_list:
                node_value_dict[replace_node(i)]=7
        for one_rxn in one_pathway:
            for i in one_rxn[1]:
                if replace_node(i) not in nodes_list:
                    nodes_list.append(replace_node(i))
                if replace_node(i) not in main_nodes_list:
                    node_value_dict[replace_node(i)]=7
            one_rxn_1=[]
            one_rxn_2=[]
            for i in one_rxn[1]:
                one_rxn_1.append(replace_node(i))
            for i in one_rxn[2]:
                one_rxn_2.append(replace_node(i))
            if set(one_rxn_1+one_rxn_2) not in link_set_list:
                link_set_list.append(set(one_rxn_1+one_rxn_2))
                link_set_s_t_list.append([set(one_rxn_1),set(one_rxn_2)])

    count_x=0
    for one_pathway in networks_bwd:
        count_x+=1
        if count_x>15:
            break
        for i in one_pathway[-1][2]:
            if replace_node(i) not in nodes_list:
                nodes_list.append(replace_node(i))
            if replace_node(i) not in main_nodes_list:
                node_value_dict[replace_node(i)]=8
        for one_rxn in one_pathway:
            for i in one_rxn[1]:
                if replace_node(i) not in nodes_list:
                    nodes_list.append(replace_node(i))
                if replace_node(i) not in main_nodes_list:
                    node_value_dict[replace_node(i)]=8
            one_rxn_1=[]
            one_rxn_2=[]
            for i in one_rxn[1]:
                one_rxn_1.append(replace_node(i))
            for i in one_rxn[2]:
                one_rxn_2.append(replace_node(i))
            if set(one_rxn_1+one_rxn_2) not in link_set_list:
                link_set_list.append(set(one_rxn_1+one_rxn_2))
                link_set_s_t_list.append([set(one_rxn_1),set(one_rxn_2)])
    #--------------------------------------------------#




    #--------------------------------------------------#

    text_file = open("data_F6P3.json", "w")
    text_file.write("{")
    text_file.write("\n")
    text_file.write("  \"nodes\": [")
    text_file.write("\n")





    print node_value_dict
    print nodes_list
    print link_set_list
    for i in nodes_list:
        if nodes_list.index(i) == len(nodes_list)-1:
            text_file.write("    {\"id\": \""+i+"\", \"group\": "+str(node_value_dict[i]) +"}" )
        else:
            text_file.write("    {\"id\": \""+i+"\", \"group\": "+str(node_value_dict[i]) +"}," )
        text_file.write("\n")
    text_file.write("  ],")
    text_file.write("\n")
    text_file.write("  \"links\": [")
    text_file.write("\n")
    for i in link_set_s_t_list:
        str1="\"source\": [ \""
        for j in i[1]: # source
            str1=str1+j+"\", \""
        str1=str1[0:-3]+" ]"

        str2="\"target\": [ \""
        for j in i[0]: # target
            str2=str2+j+"\", \""
        str2=str2[0:-3]+" ]"

        str3="\"value\": 0"
        if link_set_s_t_list.index(i)==len(link_set_s_t_list)-1:
            text_file.write("    {" + str1 + "," + str2 + "," + str3 + "}")
        else:
            text_file.write("    {" + str1 + "," + str2 + "," + str3 + "},")
        text_file.write("\n")



    '''
    for i in link_set_list:
        str1="\""
        for j in i:
            str1=str1+j+"\", \""
        str1=str1[0:-3]
        print str1
        if i == len(link_set_list)-1:
            text_file.write("    ["+str1+"]")
        else:
            text_file.write("    ["+str1+"],")
        text_file.write("\n")
        '''




    text_file.write("  ]")
    text_file.write("\n")
    text_file.write("}")
    text_file.write("\n")




if __name__ == '__main__':
    #main1()
    main2()