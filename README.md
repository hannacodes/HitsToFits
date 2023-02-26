# HitsToFits

[comment]: <> (readme template taken from https://github.com/othneildrew/Best-README-Template/blob/master/README.md)

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

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href=![Logo](https://github.com/hannacodes/HitsToFits/src/backend/static/hits2fits.png)
    <img src="" alt="banner" width="500" height="200">
  </a>

<h3 align="center">Hits To Fits</h3>

  <p align="center">
    An outfit suggester based off of song entries!
    <br />
    <a href="https://github.com/hannacodes/HitsToFits"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/hannacodes/HitsToFits">View Demo</a>
    ·
    <a href="https://github.com/hannacodes/HitsToFits/issues">Report Bug</a>
    ·
    <a href="https://github.com/hannacodes/HitsToFits/issues">Request Feature</a>
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
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    
  </ol>
</details>


<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Key Features
* Spotify API to get features about songs
* User file input to fill closet
* Remote storage of user data in Google Cloud
* AI image processing and goal based agents
* Emoji support in preview :tada:
  
<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Built With

* [![Spotify API][SpotifyAPI.com]][SpotifyAPI-url]
* [![Flask][Flask.com]][Flask-url]
* [![Google Cloud][GoogleCloud.com]][GoogleCloud-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

## Using the spotify.py module: 
Create a .env file with your SpotifyAPI Client ID & Client Secret. 

### In your file:
Import hits
Create a input field to get a link to a spotify song, or hard code it. 
In the target file, use hits.getAllData(<spotify link>)
Save this array, ex: features = hits.getAllData(<url>)
To get attributes, use the specific functions, and pass in the features array.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
// list dependecies


<!-- USAGE EXAMPLES -->
## Usage

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- CONTRIBUTORS -->
## Contributors
Lucy Hu  
Hanna Koh  
Ryan Ong  
Tiger Young  

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/hannacodes/HitsToFits.svg?style=for-the-badge
[contributors-url]: https://github.com/hannacodes/HitsToFits/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/hannacodes/HitsToFits.svg?style=for-the-badge
[forks-url]: https://github.com/hannacodes/HitsToFits/network/members
[stars-shield]: https://img.shields.io/github/stars/hannacodes/HitsToFits.svg?style=for-the-badge
[stars-url]: https://github.com/hannacodes/HitsToFits/stargazers
[issues-shield]: https://img.shields.io/github/issues/hannacodes/HitsToFits.svg?style=for-the-badge
[issues-url]: https://github.com/hannacodes/HitsToFits/issues

[product-screenshot]: images/screenshot.png

[SpotifyAPI.com]: https://img.shields.io/badge/SpotifyAPI-0d1517?style=for-the-badge&logo=spotify&logoColor=1DB954
[SpotifyAPI-url]: https://developer.spotify.com/documentation/web-api/

[Flask.com]: https://img.shields.io/badge/Flask-2a3133?style=for-the-badge&logo=flask&logoColor=FFFFFF
[Flask-url]: https://flask.palletsprojects.com/en/2.2.x/

[GoogleCloud.com]:  https://img.shields.io/badge/GoogleCloud-064f61?style=for-the-badge&logo=googlecloud&logoColor=4C8BF5
[GoogleCloud-url]: https://cloud.google.com/
