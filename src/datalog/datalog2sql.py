#!/usr/local/bin/python2.7
# encoding: utf-8
'''
datalog.datalog2sql -- convert datalog to SQL

datalog.datalog2sql is a description

It defines classes_and_methods

@author:     xiao
        
@copyright:  2013 TUW. All rights reserved.
        
@license:    BSD

@contact:    xiao@kr.tuwien.ac.at
@deffield    updated: Updated
'''

import sys
import os
import networkx as nx
import matplotlib.pyplot as plt
import pygraphviz
import datalog.yacc

def main():
    parser = datalog.yacc.parser
    datalogString = open('long.prestorew.dl').read()
    program = parser.parse(datalogString)
    G = nx.DiGraph()
    for rule in program.rules:
        for body_literal in rule.body:
            G.add_edge(body_literal.classicLiteral.atom.predicate, rule.head.predicate)
    
#    nx.draw(G)
    #nx.draw_spectral(G)
    nx.draw_graphviz(G)

    depends =  nx.topological_sort(G)

    print depends
    
    
    #print program
    
if __name__ == '__main__':
    main()
