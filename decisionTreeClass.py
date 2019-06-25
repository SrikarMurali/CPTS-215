# -*- coding: utf-8 -*-
"""
Created on Tue Nov 28 21:05:06 2017

@author: srika
"""
from collections import Counter
import simple_ml

class SimpleDecisionTree:

    _tree = {}  

    def __init__(self):
        pass
            
    def fit(self, 
            instances, 
            candidate_attribute_indexes=None,
            target_attribute_index=0,
            default_class=None):
        if not candidate_attribute_indexes:
            candidate_attribute_indexes = [i 
                                           for i in range(len(instances[0]))
                                           if i != target_attribute_index]
        self._tree = self._create_tree(instances,
                                       candidate_attribute_indexes,
                                       target_attribute_index,
                                       default_class)
        
    def _create_tree(self,
                     instances,
                     candidate_attribute_indexes,
                     target_attribute_index=0,
                     default_class=None):
        class_labels_and_counts = Counter([instance[target_attribute_index] 
                                           for instance in instances])
        if not instances or not candidate_attribute_indexes:
            return default_class
        elif len(class_labels_and_counts) == 1:
            class_label = class_labels_and_counts.most_common(1)[0][0]
            return class_label
        else:
            default_class = simple_ml.majority_value(instances, target_attribute_index)
            best_index = simple_ml.choose_best_attribute_index(instances, 
                                                               candidate_attribute_indexes, 
                                                               target_attribute_index)
            tree = {best_index:{}}
            partitions = simple_ml.split_instances(instances, best_index)
            remaining_candidate_attribute_indexes = [i 
                                                     for i in candidate_attribute_indexes 
                                                     if i != best_index]
            for attribute_value in partitions:
                subtree = self._create_tree(
                    partitions[attribute_value],
                    remaining_candidate_attribute_indexes,
                    target_attribute_index,
                    default_class)
                tree[best_index][attribute_value] = subtree
            return tree
    
    def predict(self, instances, default_class=None):
        if not isinstance(instances, list):
            return self._predict(self._tree, instances, default_class)
        else:
            return [self._predict(self._tree, instance, default_class) 
                    for instance in instances]
    
    def _predict(self, tree, instance, default_class=None):
        if not tree:
            return default_class
        if not isinstance(tree, dict):
            return tree
        attribute_index = list(tree.keys())[0]  
        attribute_values = list(tree.values())[0]
        instance_attribute_value = instance[attribute_index]
        if instance_attribute_value not in attribute_values:
            return default_class
        return self._predict(attribute_values[instance_attribute_value],
                             instance,
                             default_class)
    
    def classification_accuracy(self, instances, default_class=None):
        predicted_labels = self.predict(instances, default_class)
        actual_labels = [x[0] for x in instances]
        counts = Counter([x == y for x, y in zip(predicted_labels, actual_labels)])
        return counts[True] / len(instances), counts[True], counts[False]
    
    def pprint(self):
        print(self._tree)