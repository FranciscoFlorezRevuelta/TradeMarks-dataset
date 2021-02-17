# TradeMarks2020 dataset

The European Union Intellectual Property Office offers their database of images and metadata of trade marks registered in the EU and International Registrations designating the EU. You can download this database from [EUIPO’s Open Data Platform](https://euipo.europa.eu/ohimportal/es/open-data).

I have downloaded and curated this database in order to build a data set of labeled figurative trade marks, which I have named *TradeMarks2020* dataset, as it include figurative trade marks with filing date before 5th March 2020 (downloaded on 17 March 2020), once removed those without assigned labels. This dataset contains 853,867 figurative trade mark images and their metadata: trade mark id, filing date, text appearing in the trade mark, codes assigned based on the [Vienna Classification](https://euipo.europa.eu/ohimportal/en/vienna-classification)).

The *TradeMarks2020* dataset has been divided into three different disjoint subsets for train, validation and test purposes. This division has been carried out using [EvoSplit](https://github.com/FranciscoFlorezRevuelta/EvoSplit), a recently proposed evolutionary approach to split multi-label data sets, that tries to approximate the frequency of labels appearing in the different subsets. Using EvoSplit, 20,000 trade marks have been selected for validation and 40,000 for testing. The remaining 793,868 trade marks are used for training.

## Working with the dataset

You need to follow the next steps.

### Download the EUIPO database

1. Access [EUIPO’s Open Data Platform](https://euipo.europa.eu/ohimportal/es/open-data)
2. Download all the PIC and DIFF_PIC files under the 'Trademark' and 'InternationalRegistration' folders. This is quite laborious as there is no option to download the whole database.

### Uncompress the EUIPO database
3. Uncompress all the downloaded files into a single folder, using for instance: 
```unzip "*.zip" -d database``` 
4. The uncompressed database is structured into a folder hierarchy. The image name is not the trade mark id. This is the filing number. The trade mark id is the name of the folder in which the image is. Therefore, you must run `python organiseImages.py sourceFolder destinationFolder`. For instance, `python organiseImages.py ./database ./images` to store all the images in a single folder.

### Preprocess the images
5. Preprocess the images. You must run `python preprocessImages.py sourceFolder destinationFolder sizeImages [extendBorder(0=No,1=Yes)]`. For instance, `python preprocessImages.py ./images ./images299 299 0`. The *extendBorder* parameter fills the border with white pixels (if equal to 0) to make the image square, or tries to extend with the current color in the border of the image (if equal to 1).
  Preprocessing is required due to two main reasons:
    - In many cases, the trade marks are not centered in the image downloaded from the EUIPO database. This is frequent in filings performed in the early years when graphics manipulation and editing tools were not available; and
    - Most deep neural networks require a squared image as input.

### Use the metadata
6. You do not need to download the other files from the [EUIPO’s Open Data Platform](https://euipo.europa.eu/ohimportal/es/open-data), as I have already parsed them. The metadata files for the whole dataset and the train, validation, test subsets are available [here](https://drive.google.com/drive/folders/1OfWHG5l1LICerSQmlQ519o1raZNeblh2?usp=sharing). 
7. 

## Disclaimer

