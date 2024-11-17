# Evaluating Unidirectional Models' and Bidirectional Models' Ability to Predict Garden Path Effects
Are bidirectional LMs less surprised by garden path effects than unidirectional LMs?

## Datasets
1. Label **ROI** by swapping out \[MASK\]
2. Make garden path sentences as "unexpected" and their unambiguous equivalents as "expected" for **comparison**
3. Label **condition** of sentences: main verb/ reduced relative clause, direct object/ sentential complement, transitive/ intransitive garden path
4. Other things: sentid, contextid etc.

## Models
For this model, we are running five models of GPT-2-Small (124M parameters) and five models of BERT-Base (110M parameters), all of which can be found on [Hugging Face](https://huggingface.co/models). 

GPT-2 Small (originally from [Mistral](https://github.com/stanford-crfm/mistral?tab=readme-ov-file):
1. [Seed 21](https://huggingface.co/stanford-crfm/alias-gpt2-small-x21)
2. [Seed 49](https://huggingface.co/stanford-crfm/battlestar-gpt2-small-x49)
3. [Seed 81](https://huggingface.co/stanford-crfm/caprica-gpt2-small-x81)
4. [Seed 343](https://huggingface.co/stanford-crfm/darkmatter-gpt2-small-x343)
5. [Seed 777](https://huggingface.co/stanford-crfm/expanse-gpt2-small-x777)

BERT-Base (originally from [MultiBERTs](https://github.com/google-research/language/tree/master/language/multiberts)):
1. [Seed 0](https://huggingface.co/google/multiberts-seed_0)
2. [Seed 1](https://huggingface.co/google/multiberts-seed_1)
3. [Seed 2](https://huggingface.co/google/multiberts-seed_2)
4. [Seed 3](https://huggingface.co/google/multiberts-seed_3)
5. [Seed 4](https://huggingface.co/google/multiberts-seed_4)

## Evaluation metrics
1. Run `MinimalPair` experiments in `evaluate` and `analyze` modes on all unidirectional models.
2. Run `MinimalPair` experiments in `evaluate` and `analyze` modes on all bidirectional models.
3. Across result files from unidirectional models, calculate the average of predictability differences in ROI.
4. Across result files from bidirectional models, calculate the average of predictability differences in ROI.
5. Compare average from unidirectional models and bidirectional models.
