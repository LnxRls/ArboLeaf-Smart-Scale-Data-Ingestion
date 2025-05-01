<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![project_license][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion">
    <img src="images/logo.png" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">Python Script for Extracting Body Measurement Data from ArboLeaf Smart Scale-Generated Screenshots</h3>

  <p align="center">
    This repository provides a Python script designed to address the lack of an API in the ArboLeaf app for managing historical body measurement data. Assuming users are willing to capture a screenshot of the measurement, the script enables automated extraction of key body indicators directly from the image. Extracted data is organized and stored in a Microsoft Excel file, facilitating extended data analysis, trend tracking, and visualization beyond the app’s native functionality. 
    <br />
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion"><strong>Explore the project files »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/blob/main/images/2025_04_14.jpeg">View a screenshot of an ArboLeaf app measurement</a>
    &middot;
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    &middot;
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<? [![Product Name Screen Shot][product-screenshot]] (https://example.com)_?>

This repository provides a Python script developed to automate the processing of body composition data captured by an ArboLeaf smart scale. After completing a measurement, users can execute the script by configuring four parameters at the top: the local or network path of the raw image file, the destination path for the code generated PDF copy, the date of the measurement, and the local or network path to the target Microsoft Excel file where the parsed data will be stored. This workflow streamlines data recording, supports storage centralization, and enables further analysis.

[//]: # (Here's a blank template to get started. To avoid retyping too much info, do a search and replace with your text editor for the following: `LnxRls`, `ArboLeaf-Smart-Scale-Data-Ingestion`, `twitter_handle`, `linkedin_username`, `email_client`, `email`, `Python Script for Extracting Body Measurement Data from Scale-Generated Screenshots`, `Python Script for Extracting Body Measurement Data from Scale-Generated Screenshots`, `project_license`)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

[//]: # ([![Next][Next.js]][Next-url])
[//]: # ([![React][React.js]][React-url])
[//]: # ([![Vue][Vue.js]][Vue-url])
[//]: # ([![Angular][Angular.io]][Angular-url])
[//]: # ([![Svelte][Svelte.dev]][Svelte-url])
[//]: # ([![Laravel][Laravel.com]][Laravel-url])
[//]: # ([![Bootstrap][Bootstrap.com]][Bootstrap-url])
[![Python][python.org]][Python-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Here are the setup instructions for initializing your project in a local development environment.

Clone or download the repository to your local machine, then configure and launch it by following the example steps provided below. This process ensures a seamless local build aligned with the project specifications.

### Prerequisites

Here is a concise list of Python libraries required for the successful execution of the script in the data processing environment.
* Download the necessary Python modules or *pip install* them as the **Installation** section shows below. 
  ```sh
    os, re, cv2, img2pdf, numpy, pandas, pytesseract, PIL, pdf2image 
	```
* Tesseract OCR is an open-source, widely used optical character recognition (OCR) engine that converts text within images into machine-readable text. You'll need Tesseract installed on your machine before using this script. Tesseract is called in the Python script at the line that looks like _pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'_  
	* Tesseract-OCR can be downloaded from any of the following locations:  
		* _https://sourceforge.net/projects/tesseract-ocr.mirror/_    **(SourceForge)**  
 		* _https://github.com/tesseract-ocr/tessdoc_                  **(GitHub)**  
  		* _https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.3.0.20221214.exe_    **(Digital collections of Mannheim University Library)**  
	* To install and get introduced to Tesseract-OCR's usage basics go to _https://tesseract-ocr.github.io/tessdoc/Installation.html_ 	   

* It is highly recommended that you store the original screenshots collected from ArboLeaf, used for scale measurements, in a separate backup or network storage location. This precaution is important because the script modifies the JPEG during image processing to extract body statistics. After encountering an error or failing to execute properly the script could have passed the point it processes the image, leaving it in an altered (non-original) state. Due to that happenstance, re-executing the script could result in image processing inaccuracies or failure to process the image altogether because, in essence, it'll re-process an already processed image. Therefore, if the script fails it's recommended that you replace the image the script may have already processed with its original, from the separate backup location, before re-executing the scirpt after any coding modfications you've made to it.     
  ```sh
    os, re, cv2, img2pdf, numpy, pandas, pytesseract, PIL, pdf2image 
  
### Installation

1. Clone the repo 
   ```sh
   git clone https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion.git
   ```
2. Open the Python source code in VS Code or the IDE of your preference
3. Install the prerequisite Python modules using _pip install_ 
   ```sh
   pip install os re cv2 img2pdf numpy pandas pytesseract PIL pdf2image 
   ```
4. Change git remote url to avoid accidental pushes to base project
   ```sh
   git remote set-url origin LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion
   git remote -v # confirm the changes
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

After downloading or cloning the script, update the _Screenshot\_Network\_Location_ placeholder to the network path where the ArboLeaf app measurement screenshot (by replacing the placeholder _Screenshot\_FileName.jpeg_ with its real file name while leaving the jpeg extension) is stored on your computer. This update should be made in the _Define critical initial variables_ section of the script, a copy of which is shown below.

Similarly, replace the _Date\_Screenshot\_Taken_ placeholder with the actual date the screenshot was captured, following the _YYYY/MM/DD_ format. Finally, update the _ExcelFileName\_WhereBodyData\_WillBeSaved.xlsx_ placeholder with the desired name for the Microsoft Excel file that will store the recorded body measurement data.

While this example assumes that the _.xlsx_ file is saved in the same network location as the _.jpeg_ screenshots, you are free to specify a different location. If you choose to do so, ensure you update it in the _output\_xls_ variable accordingly.

*Define critical initial variables*  
pdf_file_path = "C:/Screenshot_Network_Location/Screenshot_FileName.pdf"  
jpg_file_path = "C:/Screenshot_Network_Location/Screenshot_FileName.jpeg"  
reading_date = "Date_Screenshot_Taken"  
  
output_xls = 'C:/Screenshot_Network_Location/ExcleFileName_WhereBodyData_WiilBeSaved.xlsx'  

After applying the placeholder updates, run the script to automatically generate a PDF version of the original JPEG and create or update the specified Excel file (automatically generated on first execution) with one appended record containing the body measurement data. Moving forward, you can execute the script repeatedly by updating the screenshot file name and capture date for each new entry.

If you need to retake the screenshot for a given date, simply replace the JPEG with the updated measurement screenshot and rerun the script without modifying any placeholders; the script will overwrite the existing record for that date in the Excel file to reflect the new data.   

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Clone Script
- [ ] Change initial parameter values
- [ ] Execute the script 
    - [ ] The .xlsx file will be automatically generated upon the initial execution of the script and a new data record with all body measurements will be appended, as it also will on each subsequent run.

See the [open issues](https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFeature`)
3. Commit your Changes (`git commit -m 'Add some NewFeature'`)
4. Push to the Branch (`git push origin feature/NewFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Top contributors:

<a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion" alt="contrib.rocks image" />
</a>



<!-- LICENSE -->
## License

Distributed under the project_license. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Know Buddy - [@AnnXiety12](https://x.com/AnnXiety12) - has no email yet.

Project Link: [https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion](https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

*@AnnXiety12* thanks for your invaluable help! I, Know Buddy, appreciate your feedback!

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion.svg?style=for-the-badge
[contributors-url]: https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion.svg?style=for-the-badge
[forks-url]: https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/network/members
[stars-shield]: https://img.shields.io/github/stars/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion.svg?style=for-the-badge
[stars-url]: https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/stargazers
[issues-shield]: https://img.shields.io/github/issues/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion.svg?style=for-the-badge
[issues-url]: https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/issues
[license-shield]: https://img.shields.io/github/license/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion.svg?style=for-the-badge
[license-url]: https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/linkedin_username
[product-screenshot]: images/screenshot.png
[Next.js]: https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=nextdotjs&logoColor=white
[Next-url]: https://nextjs.org/
[React.js]: https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB
[React-url]: https://reactjs.org/
[Vue.js]: https://img.shields.io/badge/Vue.js-35495E?style=for-the-badge&logo=vuedotjs&logoColor=4FC08D
[Vue-url]: https://vuejs.org/
[Angular.io]: https://img.shields.io/badge/Angular-DD0031?style=for-the-badge&logo=angular&logoColor=white
[Angular-url]: https://angular.io/
[Svelte.dev]: https://img.shields.io/badge/Svelte-4A4A55?style=for-the-badge&logo=svelte&logoColor=FF3E00
[Svelte-url]: https://svelte.dev/
[Laravel.com]: https://img.shields.io/badge/Laravel-FF2D20?style=for-the-badge&logo=laravel&logoColor=white
[Laravel-url]: https://laravel.com
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com
[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 
[python.org]: https://www.python.org/static/community_logos/python-logo.png
[Python-url]: https://python.org 
