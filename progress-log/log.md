# Logs


### 19-03-2016 [02:07] at Commit 118201a
- Preprocessing resize , grayimage works great with colored image 
    - reduces time and increases confidence
    - time reduced by 30 - 50 %

- Preprocessing (gray , resize , gaussian, contrast) is damaging confidence score for receipt images
    - fast  confidence is horribly low  
    - raw images gives better OCR results with high confidence score 

**Issues with Receipt Images**
-  receipts are printed using thermal printer which causes low contrast 
- thin, broken texts
- small font sizes 

<br>

**Possible Solutions:**
- minimum required preprocessing 
    - gray image + improve contract
- adding post-processing for further improvement in later stages after preprocessing is solved 


