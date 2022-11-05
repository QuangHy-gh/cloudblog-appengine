# cloudblog-appengine

<p>What is the <a href="https://cloudresumechallenge.dev/">Cloud Resume Challenge</a>?&nbsp;Forrest Brazeal created a challenge to help people prepare for a hands-on cloud career. It was in the summer of 2022 that I started this challenge, as a way to get project experience, as well as try out cloud technology. I loosely use the Cloud Resume Challenge as a basis and try adding my own twist. What was the twist you might ask, well I completed the challenge by using Python&#39;s Django framework, hence the name of this blog post, Slithering into The Cloud.</p>

<p>I found this challenge quite fruitful, yet challenging, in my case, it is even more difficult than others since I decided to deviate from what Forrest intended for us to do since I want to incorporate Django into this challenge. So let broke down my journey, I was following the GCP path:</p>

<p><strong>1. Certification - HTML-CSS - Static Website - HTTPS - DNS</strong></p>

<p>I didn&#39;t go for the certificate but goes straight into the building part, my intention was always just to try for a project that I could neatly put on my resume, I could always go for certification later on, and it might not be a Google Cloud one by then.&nbsp;</p>

<p>I used the Django framework to create a simple blog website, my resume page, and homepage, individual blog pages were written with HTML and CSS, a little bit of Django syntax. For the challenge, you would need to host your static website on Google Cloud Storage, but since I am building a simple blog here, I decided to go for a better hosting service, Google Cloud App Engine (Standard), lucky enough for me, there a <a href="https://cloud.google.com/python/django/appengine">tutorial </a>on how to deploy a Django web app on Google Cloud App Engine (GAE).&nbsp;</p>

<p>This is where I ran into my first roadblock, an interesting characteristic of cloud technology is that it is an ever-changing field, with new technology, new services being offered every now and then, and old services being updated consistently, hence why it is difficult to find an up-to-date tutorial online, or books with timeless knowledge about these specific services. Even the tutorial provided by google here has some parts that were outdated (I cannot remember which part ), which has me a little frustrated when I first try to deploy the blog, it took me a good three days of researching to get all my files right for deployment.</p>

<p>For HTTP and DNS, I was fortunate enough that GAE already provided HTTPS protocol for the web app you deploy, so I only need to buy the domain name from google. Still, GAE conveniently did this for me, meaning that I was not able to get a hand on for this part of the challenge, which I have noted and would need to do some research about it later.</p>

<p><strong>2. Javascript (visitor counter), Database, API, Python (serverless function)</strong></p>

<p>The only Javascript that I have written for this project is the top banner of the blog and in some of the applications that I imported to the blog app. Other than that, most of the code was written in Python.</p>

<p>For the visitor counter, I import the Django-Hitcount app for this, it is also possible to write a hit count by myself, too. But I found this app is better. The Django-Hitcount app was used to record my posts hit count, and store them in a database, in the first implementation, I display the hit count directly, without having built the API.</p>

<p>For the Database, Forrest recommend Google Cloud&#39;s Firestore, but I decided to go with Google Cloud&#39;s PostgreSQL. The PostgreSQL experience is actually the better part of this challenge, all I needed to do I used the PgAdmin app, and went through some tutorials to learn how to manipulate the Postgres database.</p>

<p>For the API and serverless functions, because I have used Django to build my web app, I have to use Django again to build my API app, this is my first major block since I have never written an API before, and in Django to boot, thankfully, this is not a difficult project, I was able to have my API after watching some tutorial online. In short, what I did was linked my API app to the same database as my blog app, and saved my hit counts in the JSON format using my blog posts object_id as the key fields. The hard part is linking my API app back to my Blog app, and displaying my hit counts not by the Django-Hitcount app anymore, but by using API, this part confused me the most. After some help, I was able to display my hit counts using the API, but it made me realize my knowledge gap in back-end and API, I have decided to study more on building API and back-end after this project.</p>

<p><strong>2.1 Testing</strong></p>

<p>Forrest was vague on this step since he did not specify what kind of test he want us to write, I assumed he want us to write whatever test within our ability, but I am not too comfortable writing tests for Django app, so I skipped this step.</p>

<p><strong>3. Infrastructure as Code (IaC), Source Control, CI/CD</strong></p>

<p>We finally reach the final steps of the project. In these steps, things became more abstract, as I was working within a whole new territory.&nbsp;</p>

<p>Let&#39;s take a step back and let me explain, infrastructure, source control, and ci/cd, are part of the operations (ops) side of developing and deploying apps. To gain experience in these parts, in my opinion, you need to have working experience and good mentoring. When I was working on these steps, it was frustrating because I can grasp what going on, but only loosely enough which left me desiring to know more.</p>

<p>Anyway, for IaC, I used Terraform by Hashicorp, they have great short tutorials to get you working, and good documentation. I was only having minor problems since I have almost zero experience writing scripting language, and because the scripting involves dealing with the Cloud Platform, I only kept to my comfort zone and write the bare minimum so as to not mess up my Cloud settings. I found myself having to went through other people&#39;s code, who have taken this challenge before me, quite often to have an idea of how they were using Terraform. I ended up having to write for both of my apps, the API app, and my Blog app.</p>

<p>For source control and ci/cd, I was using Cloud Build and GitHub Actions, they are surprisingly straightforward to learn and dealt with. The only problem I have was managing my app secrets with GitHub Actions, I never realized how important that step was back when I was deploying my Blog app with GAE.&nbsp;</p>

<p>That, concludes my experience with the Cloud Resume Challenge - Django version. It was a difficult yet fun challenge, it gave me a whole new appreciation for people working on the cloud and the Ops aspect of deployment. I found myself with new challenges, and new things to consider learning after my experience with the Challenge.&nbsp;</p>

<p>You can find my code to my Blog app <a href="https://github.com/QuangHy-gh/cloudblog-appengine">here </a>and my API app <a href="https://github.com/QuangHy-gh/cloudblog-api">here</a>.</p>

<p>Since hosting on GAE are costly, as they only offer free credits for the first 30 days, this blog post will also be posted on my Blog app GitHub page. I will only keep the website running through November 2022, after that, I will shut it down and delete this project from my Google Cloud accounts.</p>
