#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Marcus Bremer
# DATE CREATED: 03/02/2021                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create 
#       with this function
# 
def get_pet_labels(image_dir):
            
#Get filenames from pet_images
   in_files = listdir(image_dir)

   #Create empty dictionary
   results_dic = dict()
   
   #add key value to dictionary if it doesn't already exist
   for idx in range(0, len(in_files), 1):
          if in_files[idx][0] != ".":
            pet_label = ""
            words_list_pet_image = in_files[idx].lower().split("_")
          
            for word in words_list_pet_image:
                if word.isalpha():
                    pet_label += word + ""
          
            pet_label = pet_label.strip()
          
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
          
          else:
            print('There might be a duplicate!', 
                  in_files[idx])
          
   return results_dic
         
      
