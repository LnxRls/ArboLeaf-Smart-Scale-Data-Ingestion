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
    This repository contains a Python script developed to overcome the absence of an API in the ArboLeaf app for retrieving historical body metrics. The script enables users to extract key body measurements from a screenshot of the app’s results screen, allowing for external storage, analysis, and visualization of their data beyond the app’s native capabilities.  
    <br />
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion">View Demo</a>
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

This repository contains a Python script designed to process body composition data collected from an ArboLeaf smart scale. After taking a measurement, users can run the script after updating four parameters at the top of the script: the local/network location of the raw image file, the location where its pdf copy will be saved, the measurement's date value, and the local/network path of the final recipient Microsoft Excel file where the recorded data will be stored, enabling further analysis and tracking.

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

Here are some instructions on setting up your project locally.
Download the repo locally copy up and run it following these simple example steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* install the necessary Python modules 
  ```sh
    os, re, cv2, img2pdf, numpy, pandas, pytesseract, PIL, pdf2image 
	```

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

.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion/issues) for a full list of proposed features (and known issues).

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
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

Your Name - [@twitter_handle](https://twitter.com/twitter_handle) - email@email_client.com

Project Link: [https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion](https://github.com/LnxRls/ArboLeaf-Smart-Scale-Data-Ingestion)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* []()
* []()
* []()

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
