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
3. Uncompress all the downloaded files into a single folder. As a result you will have all the trade mark images in that folder.
4. Run to update the names of the image files and convert them all to jpg.

### Preprocess the images
Preprocessing is required due to two main reasons:
- In many cases, the trade marks are not centered in the image downloaded from the EUIPO database. This is frequent in filings performed in the early years when graphics manipulation and editing tools were not available; and
- Most deep neural networks require a squared image as input.

5. Run to preprocess the images.
## Disclaimer

