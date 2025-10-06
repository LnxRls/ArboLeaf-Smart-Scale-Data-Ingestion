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
    <img src="Images/logo.jpg" alt="Logo" width="100" height="100">
  </a>

<h3 align="center">Python Script for Extracting Body Measurement Data from ArboLeaf Smart Scale-Generated Screenshots</h3>

  <p align="center">
    This repository provides a Python script designed to address the lack of an API in the ArboLeaf app for managing historical body measurement data. Assuming users are willing to capture a screenshot of the measurement, the script enables automated extraction of key body indicators directly from the image. Extracted data is organized and stored in a Microsoft Excel file, facilitating extended data analysis, trend tracking, and visualization beyond the app’s native functionality. 
    <br />
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion"><strong>Explore the project files »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/blob/main/Images/2025_04_14.jpg">View a screenshot of an ArboLeaf app measurement</a>
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

This repository provides a Python script developed to automate the processing of body composition data captured by an ArboLeaf smart scale. After completing a measurement, end users can execute the script by configuring a couple of CLI flags: the local or network path of the raw image files, and the local or network path to the target Microsoft Excel file where the parsed data will be stored. This workflow streamlines data recording, supports storage centralization, and enables further analysis.

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

Clone or download the repository to your local machine, then configure and launch it by following the directions provided below. This process ensures a seamless local build aligned with the project specifications.

### Prerequisites

Here is a concise list of Python libraries required for the successful execution of the script in the data processing environment.
* Download the necessary Python modules or *pip install* them as the **Installation** section shows below. 
  ```sh
    os, re, cv2, img2pdf, numpy, pandas, pytesseract, PIL, pdf2image, seaborn, matplotlib, mplcursors, plotly 
	```
* Tesseract OCR is an open-source, widely used optical character recognition (OCR) engine that converts text within images into machine-readable text. You'll need Tesseract installed on your machine before using this script. Tesseract is called in the Python script at the line that looks like _pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'_  
	* Tesseract-OCR can be downloaded from any of the following locations:  
		* _https://sourceforge.net/projects/tesseract-ocr.mirror/_    **(SourceForge)**  
 		* _https://github.com/tesseract-ocr/tessdoc_                  **(GitHub)**  
  		* _https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.3.0.20221214.exe_    **(Digital collections of Mannheim University Library)**  
	* To install and get introduced to Tesseract-OCR's usage basics go to _https://tesseract-ocr.github.io/tessdoc/Installation.html_ 	   

* It is highly recommended that you store the original screenshots collected from ArboLeaf in a separate backup or network storage location. This precaution is important because the Python script modifies the JPEG it processes during image processing to extract body statistics to the point it may become unreadable. Thus, there's a strong possibility after encountering an error, or failing to execute properly, the script may have altered the image dramatically, to the point it cannot process it again. Due to that happenstance, re-executing the script could result in image processing inaccuracies or failure to process the image altogether because, in essence, it'll re-process an already processed image. Therefore, if the script fails, it's recommended that you replace the image, regardless of state, with its original from its backup location, before re-executing the script, after any coding modfications you've made to it.     
  ```sh
    os, re, cv2, img2pdf, numpy, pandas, pytesseract, PIL, pdf2image, seaborn, matplotlib, mplcursors, plotly 
  
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

After downloading or cloning the script, assign values to the only two necessary flags, namely, *--dir_path* and *--path_output_xls* and execute it as the example in the **Code Execution Example** section of the script's header shows. *--dir_path* is the local or network directory location (one or many) screenshots are stored for processing and *--path_output_xls* is the directory of the MS Excel file where the body composition data parsed from screenshots will be saved.

The script can process multiple scale screenshots as a batch. It generates a PDF version for each of the screenshot JPEGs and appends new Excel rows containing the body composition measurement data read from the JPEGs. 
If you need to retake the screenshot for a given date, simply replace the JPEG with the updated measurement screenshot and rerun the script without modifying any flags; the script will overwrite the existing Excel row for that date in the Excel file to reflect the new data. However, you must keep in mind that the script is currently designed to save the data from only one smart scale measurement per day. 

Lastly, the end user can mix screenshot retakes with new screenshots in the same folder at the *--dir_path* location before executing the script.    


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Clone Script
- [ ] Change initial parameter values
- [ ] Execute the script 
    - [ ] The .xlsx file will be automatically generated upon the initial execution of the script and a new data record with all body measurements will be appended, as it also will on each subsequent run.

See the [open issues](https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- VISUALIZATIONS - STATISTICS -->
## Visualizations - Correlation Matrices
The code generates four correlation matrices to help users analyze relationships between pairs of body statistics as data accumulates. All matrices are located in the *Images* folder. The *Static Matrices (3)* are named *Figure_x.jpg* (where *x* = 1, 2, 3) corresponding to Plots 1, 2, and 3 in the Python code and the *Interactive Matrix (1)* is the HTML file named *correlation_svg_curved_clusters.html*. The interactive matrix features are briefly summarized below:

- _Tooltip Hover_:  Upon mouse hovering over the matrix squares the tooltip displays the correlation coefficient of the x-y body-statistic pair numerically and visually.  
- _Dynamic Sizing_: Square sizes scale with the magnitude of the correlation coefficient.  
- _Cluster Toggle_: Users can click to hide/unhide clusters of squares categorized by having their perimeter colored with the same color, enabling focused exploration
		   of specific relationships.     

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
[product-screenshot]: Images/screenshot.png
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
