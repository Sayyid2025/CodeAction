# Migration Instructions from v1 to v2

This document provides guidelines for migrating from the `human_action_biomechanics_analysis.ipynb` version 1 (v1) to version 2 (v2). Below are the steps and examples illustrating the use of new modules introduced in v2.

## Overview of Changes
Version 2 introduces several new modules that enhance functionality and simplify the biomechanics analysis process. The key modules include:
- `pipeline_config`
- `biomechanics_calculator`
- `data_export`

## Migration Steps
1. **Update Your Import Statements**:
   Replace any import statements related to `human_action_biomechanics_analysis.v1` with the new modules.
   
   ```python
   # Old import from v1
   from human_action_biomechanics_analysis.v1 import some_function
   
   # New imports for v2
   from pipeline_config import PipelineConfig
   from biomechanics_calculator import BiomechanicsCalculator
   from data_export import export_data
   ```

2. **Using `pipeline_config`**:
   The `pipeline_config` module allows you to configure analysis pipelines dynamically. Here’s an example:
   
   ```python
   config = PipelineConfig(model='model_name', parameters={'param1': value1, 'param2': value2})
   config.run()
   ```

3. **Using `biomechanics_calculator`**:
   The `biomechanics_calculator` module provides methods to calculate various biomechanics metrics. For example:
   
   ```python
   calculator = BiomechanicsCalculator()
   metrics = calculator.calculate_metrics(data)
   print(metrics)
   ```

4. **Using `data_export`**:
   Exporting data has been streamlined. Here’s how you can export your results:
   
   ```python
   export_data(results, format='csv', filename='output.csv')
   ```

## Sample Code
Here is a small sample showing the usage of the new modules in action:

```python
from pipeline_config import PipelineConfig
from biomechanics_calculator import BiomechanicsCalculator
from data_export import export_data

# Configure the pipeline
config = PipelineConfig(model='new_model', parameters={'threshold': 0.5})
config.run()

# Calculate biomechanics metrics
calculator = BiomechanicsCalculator()
results = calculator.calculate_metrics(data)

# Exporting the results
export_data(results, format='json', filename='results.json')
```

Following these guidelines will help ensure a smooth transition to version 2 of the `human_action_biomechanics_analysis` module.