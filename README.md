Lab 09: CI/CD for a ML Project with GitHub Actions
What You Will Build
In this lab, you will automate a small AI project using GitHub Actions.

You will:

train a Random Forest model on the Iris dataset
test the generated output in CI
pass files between jobs using artifacts
generate an HTML report in CD
deploy the report with GitHub Pages
This lab comes after our lecture on CI/CD, so your goal is to apply the ideas in practice and clearly see the difference between:

CI: build, train, test, validate
CD: prepare the final report and deploy it
What You Should Know Before Starting
Before you begin, make sure you have:

Python 3.11
Git
a GitHub account
a GitHub repository where Actions can run
You should also know these terms from the lecture:

event
job
step
runner
artifact
continuous integration
continuous delivery / deployment
Repository Structure
ai-lab-gh-actions/
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── deploy.yml
├── assets/
├── docs/
│   └── index.html
├── src/
│   ├── model.py
│   └── render_report.py
├── tests/
│   └── test_model.py
├── .gitignore
├── README.md
└── requirements.txt
Stage 1: Explore the Project
Start by reading these files:

src/model.py
tests/test_model.py
docs/index.html
.github/workflows/ci.yml
.github/workflows/deploy.yml
As you read, identify the role of each file.

Stage 2: Run the Project Locally
Run the project locally before relying on GitHub Actions.

Install the dependencies:

pip install -r requirements.txt
Train the model:

python src/model.py
Run the tests:

pytest tests/test_model.py
After that, check the assets/ folder.

You should see generated output such as:

the trained model file
a metrics file
a confusion matrix image
Stage 3: Read the CI Workflow
Open .github/workflows/ci.yml.

Notice that CI is split into multiple jobs:

build
test
report
Follow the flow:

build trains the model and creates the output files
test downloads those files and validates them
report checks that the report inputs are ready for deployment
Also notice the use of:

needs
upload-artifact
download-artifact
Important:

CI should validate work
CI should not keep rewriting the repository
CI should fail early if something is wrong
Stage 4: Read the CD Workflow
Open .github/workflows/deploy.yml.

This workflow is different from CI.

Its job is not to retrain the model. Its job is to:

wait for a successful CI run on main
download the validated artifact
generate the final HTML report
deploy it to GitHub Pages
Important:

CD uses the result of CI
CD should not repeat work that CI already completed
deployment should happen only after validation succeeds
Stage 5: Push and Observe the Pipelines
Push your repository to GitHub and open the Actions tab.

Watch what happens:

the CI workflow starts on push
jobs run in sequence
the CD workflow starts only after CI succeeds on main
As you watch the workflows, pay attention to:

which job starts first
how needs controls the order
where the final report is generated
Stage 6: Enable GitHub Pages
Open Settings -> Pages.

Set Build and deployment to GitHub Actions.

Once deployment succeeds, open the published page.

Check that:

the accuracy is shown correctly
the value is not hard-coded
the confusion matrix image appears
the report reflects the pipeline output
Stage 7: Trigger a Failure on Purpose
CI is useful because it catches problems before deployment.

To test that idea, create a failure intentionally.

Example:

change the minimum accuracy threshold from 0.90 to 1.01
Then push the change and observe the result.

After the failure, restore the correct threshold and push again.

Stage 8: Optional Extension
If you finish early, choose one small improvement:

Add one more metric to the HTML report.
Add one more test for the generated files.
Improve the report text so it explains what the confusion matrix means.
This part is optional. Complete the main lab first.

What You Should Learn from This Lab
By the end of the lab, you should be able to explain:

the difference between CI and CD
why artifacts are useful
why jobs are separated
why deployment should use validated outputs
why generated files should not be committed back by CI in this case
Submission
Submit:

your GitHub repository URL
a screenshot of a successful CI run
a screenshot of the deployed GitHub Pages report
a short note explaining how your CI works
a short note explaining how your CD works
one issue you faced and how you solved it
Before you submit, make sure you can clearly explain:

what CI does in this project
what CD does in this project
