# End to end project using pipelines from data ingestion, model training, evaluation and prediction. The prediction is done using an App. A docker was also built and deployed in a Google Cloud Run service.

The trained model classifies images into two classes "Healthy" or "Coccidiosis"(the task itself not relevant here).

## Workflows
1. For every pipeline the artifact configuration (input/outputs destination) is added to the config.yaml.
2. Then an entity is created to hold the config variables revelant to each pipeline.
3. The configuration manager is responsible for reading the config.yaml and creating the entities for each pipeline.
4. The pipeline is coded using the components classes and the entities.
5. Finally the main.py executes all pipelines.



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/entbappy/Chicken-Disease-Classification--Project

### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag









