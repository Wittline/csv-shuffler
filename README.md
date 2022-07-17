# csv-shuffler
A tool to automatically Shuffle lines in a .csv files

![image](https://user-images.githubusercontent.com/8701464/179423167-35b1780b-5aa3-46e4-ad19-eec4ca8ba820.png)



<div class="cell markdown" id="H9YNJNwhsVmc">

# **Installing *csv\_shuffler* 🔧**

</div>

<div class="cell code" data-execution_count="5" data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="hcFSBcqInabZ" data-outputId="becaeb22-455c-4c7d-e0af-34b42f13ed6e">

``` python
pip install csv-shuffler
```

<div class="output stream stdout">

    Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/
    Collecting csv-shuffler
      Downloading csv_shuffler-0.0.3-py3-none-any.whl (2.9 kB)
    Installing collected packages: csv-shuffler
    Successfully installed csv-shuffler-0.0.3

</div>

</div>

<div class="cell markdown" id="kz-w4ZRssY2b">

# **Importing *csv\_shuffler* library ⚡**

</div>

<div class="cell code" data-execution_count="6" id="VML2Xlocnu0h">

``` python
from csv_shuffler import csv_shuffler
```

</div>

<div class="cell markdown" id="N_UOwTIcshpz">

# **Setting *csv\_shuffler* configuration ✍**

</div>

<div class="cell code" id="63JsnM-Qn5gI">

``` python
shuffler = csv_shuffler.ShuffleCSV(input_file='/content/sample_data/mnist_train_small.csv',header=True, batch_size=20000)
```

</div>

<div class="cell markdown" id="Mhcama3ksvk7">

# **Run shuffler 🏃**

</div>

<div class="cell code" data-execution_count="9" data-colab="{&quot;base_uri&quot;:&quot;https://localhost:8080/&quot;}" id="mXsyl5Zwst1C" data-outputId="e34ddaad-ffb9-4efc-ee0d-d10764946b65">

``` python
shuffler.shuffle_csv()
```

<div class="output execute_result" data-execution_count="9">

    19999

</div>

</div>

## Contributing and Feedback
Any ideas or feedback about this repository?. Help me to improve it.

## Authors
- Created by <a href="https://twitter.com/RamsesCoraspe"><strong>Ramses Alexander Coraspe Valdez</strong></a>
- Created on 2022

## License
This project is licensed under the terms of the MIT License.
