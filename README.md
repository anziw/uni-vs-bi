# Evaluating Unidirectional Models' and Bidirectional Models' Ability to Predict Garden Path Effects
Are bidirectional LMs less surprised by garden path effects than unidirectional LMs?

## Evaluation metrics
1. Run 'MinimalPair' experiments in 'evaluate' and 'analyze' modes on all unidirectional models.
2. Run 'MinimalPair' experiments in 'evaluate' and 'analyze' modes on all bidirectional models.
3. Across result files from unidirectional models, calculate the average of predictability differences in ROI.
4. Across result files from bidirectional models, calculate the average of predictability differences in ROI.
5. Compare average from unidirectional models and bidirectional models.
