# Evaluating Unidirectional Models' and Bidirectional Models' Ability to Predict Garden Path Effects
Are bidirectional LMs less surprised by garden path effects than unidirectional LMs?

## Datasets
1. Label **ROI** by swapping out \[MASK\]
2. Make garden path sentences as "unexpected" and their unambiguous equivalents as "expected" for **comparison**
3. Label **condition** of sentences: main verb/ reduced relative clause, direct object/ sentential complement, transitive/ intransitive garden path
4. Other things: sentid, contextid etc.


## Evaluation metrics
1. Run `MinimalPair` experiments in `evaluate` and `analyze` modes on all unidirectional models.
2. Run `MinimalPair` experiments in `evaluate` and `analyze` modes on all bidirectional models.
3. Across result files from unidirectional models, calculate the average of predictability differences in ROI.
4. Across result files from bidirectional models, calculate the average of predictability differences in ROI.
5. Compare average from unidirectional models and bidirectional models.
