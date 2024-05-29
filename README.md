# End to end project using pipelines from data ingestion, model training, evaluation and prediction. The prediction is done using an App. A docker was also built and deployed in a Google Cloud Run service.

The trained model classifies images into two classes "Healthy" or "Coccidiosis"(the task itself not relevant here). This is a template project to use for any machine learning pipeline and prediction app.

## Workflows
1. For every pipeline the artifact configuration (input/outputs destination) is added to the config.yaml. (Open and give a quick look at config.yaml)
2. Then an entity is created to hold the config variables revelant to each pipeline. (Open config.yamlsrc/ccnClassifier/entity/config_entity to see)
3. The configuration manager is responsible for reading the config.yaml and creating the entities for each pipeline. (located at src/cnnClassifier/config/configuration.py)
4. The pipeline is coded using the components classes and the entities. (check pipelines at src/cnnClassifier/pipeline/)
5. Finally the main.py executes all pipelines.

The code is pretty simple to follow. All pipelines are built in the same way following the workflow (add paths to -> config.yaml->entity->config manager->pipeline->main.py)

# How to run the prediction app?

### STEP 01 - Clone the repository

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```
### STEP 03- Run the app
```bash
python app.py
```
### STEP 04 - Go to localhost:8080

# How to run the training pipeline?
Just execute the main.py.
```bash
python main.py
```
### To run the pipeline for training and saving a model you can use DVC with the dvc config coded in dvc.yaml. Just move to the project repo in command line and execute the following code.
```bash
dvc init
dvc repro
dvc dag
```








