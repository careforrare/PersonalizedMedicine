---
title: Create an App on FeatureCloud
weight: 4
---

### Register on FeatureCloud

1. Go to https://featurecloud.ai/ and click on the login button in the right upper corner.
2. Click on *Sign up*.
3. Make sure that you register as “App Developer”. If you want to publish, select the respective option.

### Add an App

1. Go to https://featurecloud.ai/app-store.
2. Click on the Development menu option. See:{{% imgproc development-menu-option Fit "500x200" %}}{{% /imgproc %}}
3. Click on *Add App*.
4. Fill in the details of your app and choose an image name. Note: that no frontend is needed for our purposes and the URL link may direct to our GitHub repository.

### Publish an App

1. Prerequisites
    <ol type="a">
    <li>Install FeatureCloud pip package: <code>pip install feacturecloud</code></li>
    <li>Start Controller: <code>feacturecloud controller start</code></li>
    </ol>
2. Implement your application
    <ol type="a">
    <li>Create and implement an application based on a template:<br/><code>featurecloud app new --template-name=app-blank app-blank</code></li>
    <li>Build your application:<br/><code>featurecloud app build ./app-blank my-app`</code></li>
    <li>Test your application with Testbed:<br/><code>featurecloud test start --controller-host=http://localhost:8000 --app-image=my-app --query-interval=1 --client-dirs=.,.</code></li>
    </ol>
    Note 1: you may have register first with docker login featurecloud.ai.

### Find an App

To see your app in the store you must tick the respective option:
{{% imgproc find-app Fit "300x150" %}}{{% /imgproc %}}

### Run an App

1. To run an app you created, click on the Projects tab.
2. Click on Create and name you project.
3. Click on the blue button with arrow next to your app. Make you pushed an updated image of your app.

### Helpful Links

https://featurecloud.ai/developers

https://github.com/FeatureCloud/FeatureCloud

https://featurecloud.ai/assets/developer_documentation/getting_started.html

 

 
  
 
