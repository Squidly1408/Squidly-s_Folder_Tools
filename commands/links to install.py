import tkinter as tk
from tkinter import ttk
import webbrowser


class SoftwareResourceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Software and Resource Finder")
        self.root.geometry("500x400")
        self.root.configure(bg="#171717")  # Set background color

        # Search box
        self.search_var = tk.StringVar()
        search_frame = tk.Frame(root, bg="#171717")
        search_frame.pack(pady=10, padx=10, anchor="w")

        self.search_entry = tk.Entry(
            search_frame,
            textvariable=self.search_var,
            bg="#171717",
            fg="white",
            borderwidth=0,
            insertbackground="white",
            font=("Arial", 12),
        )
        self.search_entry.insert(0, "Search for software, package, or language...")
        self.search_entry.bind("<FocusIn>", self.clear_placeholder)
        self.search_entry.bind("<FocusOut>", self.add_placeholder)
        self.search_entry.pack(fill="x", expand=True)

        # Divider
        divider = tk.Frame(root, height=2, bg="gray")
        divider.pack(fill="x", padx=10, pady=10)

        # Listbox for software/resources
        self.resources_listbox = tk.Listbox(
            root,
            bg="#171717",
            fg="white",
            selectbackground="#00796b",
            selectforeground="white",
            activestyle="none",
            highlightthickness=0,
            borderwidth=0,
            font=("Arial", 12),
        )
        self.resources_listbox.pack(fill="both", expand=True, padx=10, pady=5)

        # Populate with predefined options
        self.resources = {
            # Software
            "Python": "https://www.python.org/downloads/",
            "Java": "https://www.java.com/en/download/",
            "Node.js": "https://nodejs.org/en/download/",
            "Git": "https://git-scm.com/downloads",
            "Visual Studio Code": "https://code.visualstudio.com/",
            "IntelliJ IDEA": "https://www.jetbrains.com/idea/download/",
            "Eclipse": "https://www.eclipse.org/downloads/",
            "Android Studio": "https://developer.android.com/studio",
            "Docker": "https://www.docker.com/get-started",
            "Postman": "https://www.postman.com/downloads/",
            "Slack": "https://slack.com/downloads",
            "Zoom": "https://zoom.us/download",
            "Sublime Text": "https://www.sublimetext.com/",
            "Vim": "https://www.vim.org/download.php",
            "Xcode": "https://developer.apple.com/xcode/",
            "PyCharm": "https://www.jetbrains.com/pycharm/download/",
            "RStudio": "https://posit.co/download/rstudio-desktop/",
            "Unity": "https://unity.com/download",
            "Blender": "https://www.blender.org/download/",
            "GIMP": "https://www.gimp.org/downloads/",
            "Notepad++": "https://notepad-plus-plus.org/downloads/",
            "Tableau": "https://www.tableau.com/products/desktop",
            "Jupyter Notebook": "https://jupyter.org/install",
            "MATLAB": "https://www.mathworks.com/products/matlab.html",
            "Wireshark": "https://www.wireshark.org/download.html",
            "Krita": "https://krita.org/en/download/krita-desktop/",
            "Inkscape": "https://inkscape.org/release/inkscape-1.1.2/",
            "Figma": "https://www.figma.com/downloads/",
            "Trello": "https://trello.com/en/platforms",
            "Notion": "https://www.notion.so/product",
            "Evernote": "https://evernote.com/download",
            "Airtable": "https://airtable.com/download",
            "Miro": "https://miro.com/download/",
            "Lucidchart": "https://www.lucidchart.com/pages/download",
            "Asana": "https://asana.com/download",
            "Slack": "https://slack.com/downloads",
            "Microsoft Teams": "https://www.microsoft.com/en-us/microsoft-teams/download-app",
            "Zoom": "https://zoom.us/download",
            "Fritz": "https://www.fritz.com/en/downloads",
            "OBS Studio": "https://obsproject.com/download",
            "Final Cut Pro": "https://www.apple.com/final-cut-pro/",
            "Adobe Premiere Pro": "https://www.adobe.com/products/premiere.html",
            "Autodesk Maya": "https://www.autodesk.com/products/maya/overview",
            "AutoCAD": "https://www.autodesk.com/products/autocad/overview",
            "Blender": "https://www.blender.org/download/",
            "GIMP": "https://www.gimp.org/downloads/",
            "VLC Media Player": "https://www.videolan.org/vlc/",
            "Steam": "https://store.steampowered.com/about/",
            "Epic Games Launcher": "https://www.unrealengine.com/download",
            "Unity": "https://unity.com/download",
            "GameMaker Studio 2": "https://www.yoyogames.com/get",
            "CryEngine": "https://www.cryengine.com/download",
            "Godot": "https://godotengine.org/download",
            # Coding Languages
            "Python": "https://www.python.org/downloads/",
            "JavaScript": "https://www.javascript.com/",
            "C": "https://www.cprogramming.com/download.html",
            "C++": "https://isocpp.org/get-started",
            "Java": "https://www.java.com/en/download/",
            "Ruby": "https://www.ruby-lang.org/en/documentation/installation/",
            "Swift": "https://www.swift.org/download/",
            "Go": "https://golang.org/dl/",
            "R": "https://cran.r-project.org/mirrors.html",
            "Rust": "https://www.rust-lang.org/learn/get-started",
            "PHP": "https://www.php.net/downloads.php",
            "Kotlin": "https://kotlinlang.org/docs/tutorials/command-line.html",
            "TypeScript": "https://www.typescriptlang.org/download",
            "Perl": "https://www.perl.org/get.html",
            "Lua": "https://www.lua.org/download.html",
            "SQL": "https://www.mysql.com/downloads/",
            "HTML5": "https://www.w3.org/TR/html5/",
            "CSS3": "https://www.w3.org/Style/CSS/",
            "Shell Script": "https://www.gnu.org/software/bash/",
            "Julia": "https://julialang.org/downloads/",
            "Dart": "https://dart.dev/get-dart",
            "Haskell": "https://www.haskell.org/downloads/",
            "MATLAB": "https://www.mathworks.com/products/matlab.html",
            "VHDL": "https://www.xilinx.com/products/design-tools/vhdl.html",
            "SAS": "https://www.sas.com/en_us/software.html",
            "F#": "https://fsharp.org/",
            "Scala": "https://www.scala-lang.org/download/",
            "Elixir": "https://elixir-lang.org/install.html",
            "Erlang": "https://www.erlang.org/downloads",
            "VHDL": "https://www.xilinx.com/products/design-tools/vhdl.html",
            "Solidity": "https://soliditylang.org/",
            "Objective-C": "https://developer.apple.com/documentation/objectivec",
            "Racket": "https://racket-lang.org/download/",
            "OCaml": "https://ocaml.org/docs/install.html",
            "Ada": "https://www.adacore.com/download",
            "D": "https://dlang.org/download.html",
            "Crystal": "https://crystal-lang.org/install/",
            "Nim": "https://nim-lang.org/install.html",
            "Groovy": "https://groovy-lang.org/download.html",
            "Clojure": "https://clojure.org/guides/getting_started",
            "Smalltalk": "https://www.gnu.org/software/smalltalk/",
            "Prolog": "https://www.swi-prolog.org/Download.html",
            "Vala": "https://wiki.gnome.org/Projects/Vala",
            "Tcl": "https://www.tcl.tk/software/tcltk/download.html",
            "Forth": "https://www.forth.com/starting-forth/",
            "Logo": "https://www.softronix.com/logo.html",
            "Bash": "https://www.gnu.org/software/bash/",
            "Zig": "https://ziglang.org/download/",
            "ActionScript": "https://www.adobe.com/products/flashplayer.html",
            "PostScript": "https://www.adobe.com/products/postscript.html",
            # Frameworks
            "Django": "https://www.djangoproject.com/download/",
            "Flask": "https://flask.palletsprojects.com/en/2.0.x/installation/",
            "React": "https://reactjs.org/docs/getting-started.html",
            "Vue.js": "https://vuejs.org/guide/installation.html",
            "Angular": "https://angular.io/guide/setup-local",
            "Spring Boot": "https://spring.io/projects/spring-boot",
            "Laravel": "https://laravel.com/docs/8.x/installation",
            "Express.js": "https://expressjs.com/en/starter/installing.html",
            "Ruby on Rails": "https://rubyonrails.org/",
            "ASP.NET": "https://dotnet.microsoft.com/en-us/apps/aspnet",
            "Flutter": "https://flutter.dev/docs/get-started/install",
            "Bootstrap": "https://getbootstrap.com/docs/5.0/getting-started/introduction/",
            "Foundation": "https://get.foundation/sites.html",
            "Ember.js": "https://emberjs.com/installation/",
            "Xamarin": "https://dotnet.microsoft.com/en-us/apps/xamarin",
            "Next.js": "https://nextjs.org/docs/getting-started",
            "Tailwind CSS": "https://tailwindcss.com/docs/installation",
            "NestJS": "https://nestjs.com/",
            "Svelte": "https://svelte.dev/docs",
            "Socket.io": "https://socket.io/docs/v4/",
            "Laravel": "https://laravel.com/docs",
            "Symfony": "https://symfony.com/download",
            "Redux": "https://react-redux.js.org/introduction/getting-started",
            "TensorFlow": "https://www.tensorflow.org/install",
            "Vuex": "https://vuex.vuejs.org/",
            "Vue Router": "https://router.vuejs.org/",
            "Redux": "https://redux.js.org/introduction/getting-started",
            "AngularJS": "https://angularjs.org/",
            "Ruby on Rails": "https://rubyonrails.org/",
            "Meteor.js": "https://www.meteor.com/",
            "Gatsby.js": "https://www.gatsbyjs.com/docs/",
            "Nuxt.js": "https://nuxtjs.org/docs/",
            "Electron": "https://www.electronjs.org/docs",
            "Jest": "https://jestjs.io/docs/getting-started",
            "GraphQL": "https://graphql.org/learn/",
            "Next.js": "https://nextjs.org/docs/getting-started",
            "Tailwind CSS": "https://tailwindcss.com/docs/installation",
            "Express.js": "https://expressjs.com/en/starter/installing.html",
            "Laravel": "https://laravel.com/docs/8.x/installation",
            "Django": "https://www.djangoproject.com/start/",
            "Flask": "https://flask.palletsprojects.com/en/2.0.x/installation/",
            "Socket.io": "https://socket.io/docs/v4/",
            "Spring Boot": "https://spring.io/projects/spring-boot",
            "Pytest": "https://docs.pytest.org/en/stable/getting-started.html",
            "FastAPI": "https://fastapi.tiangolo.com/",
            "Zend Framework": "https://framework.zend.com/",
            "Phalcon": "https://phalcon.io/en-us/",
            "Phoenix": "https://www.phoenixframework.org/",
            "Sails.js": "https://sailsjs.com/documentation/getting-started",
            # Data Science & Machine Learning Packages
            "NumPy": "https://numpy.org/install/",
            "Pandas": "https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html",
            "SciPy": "https://scipy.org/install/",
            "Matplotlib": "https://matplotlib.org/stable/users/installing.html",
            "Seaborn": "https://seaborn.pydata.org/installing.html",
            "Scikit-learn": "https://scikit-learn.org/stable/install.html",
            "Keras": "https://keras.io/getting_started/",
            "PyTorch": "https://pytorch.org/get-started/locally/",
            "OpenCV": "https://opencv.org/releases/",
            "TensorFlow": "https://www.tensorflow.org/install",
            "XGBoost": "https://xgboost.readthedocs.io/en/stable/install.html",
            "LightGBM": "https://lightgbm.readthedocs.io/en/latest/Installation-Guide.html",
            "NLTK": "https://www.nltk.org/install.html",
            "SpaCy": "https://spacy.io/installation",
            "Gensim": "https://radimrehurek.com/gensim/install.html",
            "statsmodels": "https://www.statsmodels.org/stable/install.html",
            "Scrapy": "https://scrapy.org/",
            "PySpark": "https://spark.apache.org/docs/latest/api/python/getting_started/index.html",
            "MLlib": "https://spark.apache.org/mllib/",
            "Pillow": "https://pillow.readthedocs.io/en/stable/installation.html",
            "Plotly": "https://plotly.com/python/getting-started/",
            "Dash": "https://dash.plotly.com/introduction",
            "Bokeh": "https://bokeh.org/install/",
            "PyCaret": "https://pycaret.org/install/",
            "Dask": "https://dask.org/install/",
            "Hugging Face Transformers": "https://huggingface.co/docs/transformers/installation",
            "OpenAI Gym": "https://gym.openai.com/",
            "Scikit-Image": "https://scikit-image.org/",
            "Pytorch Lightning": "https://pytorch-lightning.readthedocs.io/en/stable/",
            "Keras": "https://keras.io/getting_started/",
            "XGBoost": "https://xgboost.readthedocs.io/en/stable/install.html",
            "LightGBM": "https://lightgbm.readthedocs.io/en/latest/Installation-Guide.html",
            "Dask": "https://dask.org/install/",
            "MLflow": "https://mlflow.org/",
            "Optuna": "https://optuna.org/",
            "Statsmodels": "https://www.statsmodels.org/stable/install.html",
            "Seaborn": "https://seaborn.pydata.org/installing.html",
            "Plotly": "https://plotly.com/python/getting-started/",
            "Bokeh": "https://bokeh.org/install/",
            "Dash": "https://dash.plotly.com/introduction",
            "SpaCy": "https://spacy.io/installation",
            "TensorFlow Lite": "https://www.tensorflow.org/lite/guide",
            "PIL/Pillow": "https://pillow.readthedocs.io/en/stable/installation.html",
            "Caffe": "http://caffe.berkeleyvision.org/installation.html",
            "Theano": "http://deeplearning.net/software/theano/",
            "OpenCV": "https://opencv.org/releases/",
            "PyCaret": "https://pycaret.org/install/",
            "Pandas Profiling": "https://pandas-profiling.github.io/pandas-profiling/docs/",
            "Yellowbrick": "https://www.scikit-yb.org/en/latest/",
            "Vaex": "https://vaex.io/docs/install.html",
            "Gensim": "https://radimrehurek.com/gensim/install.html",
            # DevOps Tools
            "Docker": "https://www.docker.com/get-started",
            "Kubernetes": "https://kubernetes.io/docs/setup/",
            "Jenkins": "https://www.jenkins.io/download/",
            "Terraform": "https://www.terraform.io/downloads.html",
            "Ansible": "https://www.ansible.com/products/ansible",
            "Chef": "https://www.chef.io/products/chef-infra",
            "Puppet": "https://puppet.com/download-puppet-enterprise/",
            "GitLab": "https://about.gitlab.com/install/",
            "CircleCI": "https://circleci.com/docs/2.0/install/",
            "Travis CI": "https://travis-ci.org/",
            "Docker Compose": "https://docs.docker.com/compose/install/",
            "Prometheus": "https://prometheus.io/docs/prometheus/latest/installation/",
            "Grafana": "https://grafana.com/grafana/download",
            "New Relic": "https://docs.newrelic.com/docs/agents",
            "Datadog": "https://www.datadoghq.com/",
            "Nagios": "https://www.nagios.org/downloads/",
            "Sentry": "https://sentry.io/",
            "AWS CLI": "https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html",
            "Azure CLI": "https://learn.microsoft.com/en-us/cli/azure/install-azure-cli",
            "Google Cloud SDK": "https://cloud.google.com/sdk/docs/install",
            "Vagrant": "https://www.vagrantup.com/downloads",
            "Homebrew": "https://brew.sh/",
            "Slack CI/CD": "https://slack.com/help/articles/213868947-Integrate-your-build-system-with-Slack",
            "SonarQube": "https://www.sonarqube.org/downloads/",
        }

        self.load_resources()

        # Bind events
        self.search_var.trace("w", self.update_list)
        self.resources_listbox.bind("<Double-1>", self.open_website)

    def clear_placeholder(self, event):
        """Clear the placeholder text in the search box."""
        if self.search_entry.get() == "Search for software, package, or language...":
            self.search_entry.delete(0, tk.END)
            self.search_entry.config(fg="white")

    def add_placeholder(self, event):
        """Add the placeholder text if the search box is empty."""
        if not self.search_entry.get():
            self.search_entry.insert(0, "Search for software, package, or language...")
            self.search_entry.config(fg="grey")

    def load_resources(self):
        """Load predefined resources into the listbox."""
        self.resources_listbox.delete(0, tk.END)
        for resource in self.resources:
            self.resources_listbox.insert(tk.END, resource)

    def update_list(self, *args):
        """Update the list based on the search box input."""
        search_term = self.search_var.get().lower()
        filtered_resources = [
            resource for resource in self.resources if search_term in resource.lower()
        ]
        self.resources_listbox.delete(0, tk.END)
        for resource in filtered_resources:
            self.resources_listbox.insert(tk.END, resource)

    def open_website(self, event=None):
        """Open the website associated with the selected resource."""
        selected_resource = self.resources_listbox.get(tk.ACTIVE)
        if selected_resource:
            url = self.resources[selected_resource]
            webbrowser.open(url)


# Function to run the application
def run_gui():
    root = tk.Tk()
    app = SoftwareResourceApp(root)
    root.mainloop()


if __name__ == "__main__":
    run_gui()
