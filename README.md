# 5 September 2023:

I was able to get all the functions to generate the correct output as the test file with the exception of intradaysd

Started adding some new functions to further play with the data


# cgmquantify: python package for analyzing glucose and glucose variability
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Continuous glucose monitoring (CGM) systems provide real-time, dynamic glucose information by tracking interstitial glucose values throughout the day. Glycemic variability, also known as glucose variability, is an established risk factor for hypoglycemia (Kovatchev) and has been shown to be a risk factor in diabetes complications. Over 20 metrics of glycemic variability have been identified.

Here, we provide functions to calculate glucose summary metrics, glucose variability metrics (as defined in clinical publications), and visualizations to visualize trends in CGM data.

This module currently works with [Dexcom G6 data](https://www.dexcom.com/get-started-cgm/111?sfc=7014y000000yxYNAAY&gclid=EAIaIQobChMI4ejrpLHQ7gIVhbzICh1ntQ2hEAAYASAAEgKghfD_BwE).

The cgmquantify package is [now available in R!](https://CRAN.R-project.org/package=cgmquantify)

#### [User Guide](https://github.com/brinnaebent/cgmquantify/wiki/User-Guide)
#### [Issue Tracking](https://github.com/brinnaebent/cgmquantify/issues)

#### Installation:
* **Recommended:** Use the following code in Google Collab https://colab.research.google.com/
```
!git clone https://github.com/90oak/cgmquantify.git
import sys
sys.path.append("/content/cgmquantify")
import cgmquantify as cgm
dir(cgm) #if install worked then you will get a list of cgmquantify functions
```

#### Dependencies: (these will be downloaded upon installation with pip)
pandas, numpy, matplotlib, statsmodels, datetime, plotly

>Coming soon -
>* Currently only supports Dexcom CGM, more CGM coming soon
>* Integration with food logs, myFitnessPal food logs
>* Machine Learning methods for discovering trends in CGM data




