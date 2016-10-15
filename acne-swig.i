%module acne
 %{
 /* Includes the header in the wrapper code */
 #include "acne.h"
 %}
 
 /* Parse the header file to generate wrappers */
 %include "acne.h"