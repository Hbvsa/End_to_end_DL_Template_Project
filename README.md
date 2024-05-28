# End to end project using pipelines from data ingestion, model training, evaluation and prediction. The prediction is done using an App. A docker was also built and deployed in a Google Cloud Run service.

The trained model classifies images into two classes "Healthy" or "Coccidiosis"(the task itself not relevant here).

## Workflows
1. For every pipeline the artifact configuration (input/outputs destination) is added to the config.yaml.
2. Then an entity is created to hold the config variables revelant to each pipeline.
3. The configuration manager is responsible for reading the config.yaml and creating the entities for each pipeline.
4. The pipeline is coded using the components classes and the entities.
5. Finally the main.py executes all pipelines.



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
### To run the pipeline for training and saving a model you can use DVC with the dvc config coded in dvc.yaml. Execute the following commands in the project repo.
```bash
dvc init
dvc repro
dvc dag
```








