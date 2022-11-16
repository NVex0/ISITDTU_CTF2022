Through enc.py, i know how flag was killed:

**flag.png[rgba]** `(xor)`  **Rrgba** -> **out.png[rgba]**

<sub>**Rrgba** : pseudo-random rgba number generated from:</sub>

![Screenshot (2765)](https://user-images.githubusercontent.com/113530029/202249633-77aeb4cb-819c-42b5-a8ea-e835ca760cba.png)

So, to recover the flag, just do:

***out.png[rgba]** `(xor)` **Rrgba** -> **flag.png[rgba]***

We have **out.png**, but the **Rrgba** ?

To get the Rrgba values, do the same way as above:

***out.png[rgba]** `(xor)` **flag[rgba]** -> **Rrgba***

Since we only have the remaining part of flag **part.png**, that means we can only recover same part of **Rrgba**:

***out.png[rgba]** `(xor)` **part.png[rgba]** -> **part of Rrgba***

So i came up with using `Mersenne Twister Predictor` to recover whole Rrgba. 

<sub>`Mersenne Twister Predictor`: It required first 624 values from same seed to predict every next "random" value.</sub>


Look at the **part.png**, it is the correct head part of flag (x axis). The image contains 518400 rgba values (size 720x720). Following y axis, correct part account for about 1/20 im not sure XD. But it definitely greater than 1 rgba line (1/720) -> first 624 **Rrgba** values are correct.

Using https://github.com/kmyk/mersenne-twister-predictor to get full **Rrgba**:

![Screenshot (2767)](https://user-images.githubusercontent.com/113530029/202268397-5c581101-e81d-4be1-87c7-bc3dd68303d0.png)

After got the **Rrgba**, xoring with **out.png** to recover flag:

![Screenshot (2769)](https://user-images.githubusercontent.com/113530029/202270260-828b209d-41a5-4118-84db-5185321ac5b7.png)

Here we go:

![flag2](https://user-images.githubusercontent.com/113530029/202271281-7b7753fa-4a75-49cf-b749-6b2e80f3c77a.png)

Flag : ISITDTU{DC_DC34s3d_h4v3_y0u_r34d?}


