#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask
from flask import request, render_template
from tensorflow.keras.models import load_model


# In[19]:


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        NPTA = request.form.get("NPTA")
        TLTA = request.form.get("TLTA")
        WCTA = request.form.get("WCTA")
        print(NPTA, TLTA, WCTA)
        model=load_model("bankruptcy")
        if NPTA == '' or TLTA == '' or WCTA == '':
            s = "Please Enter a Valid Number for Each"
        else:    
            pred=model.predict([[float(NPTA), float(TLTA), float(WCTA)]])
            s= "The Predicted Bankruptcy Score is: " + str(pred)
        return(render_template("index.html", result = s))
    else:
        return(render_template("index.html", result = "Predicted Bankruptcy Score"))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:




