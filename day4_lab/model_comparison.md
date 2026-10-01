# Open Model Comparison

| Model family | License | Commercial use | Redistribution | Tool calling | Notes |
|---|---|---|---|---|---|
| Qwen | Apache 2.0 for the referenced open models | Yes, subject to licence/model terms | Yes, subject to licence terms | Supported by many Qwen instruct models | Strong general-purpose and multilingual models |
| Mistral | Apache 2.0 for many open models; check the specific model | Depends on the specific model licence | Depends on the specific model licence | Supported by several instruct models | Licence varies across Mistral releases |
| IBM Granite | Apache 2.0 for the referenced open models | Yes, subject to licence terms | Yes, subject to licence terms | Supported by Granite instruct/tool models | Designed for enterprise and business use cases |
| gpt-oss | Apache 2.0 | Yes, subject to licence terms | Yes, subject to licence terms | Designed to support tool use | Open-weight reasoning models from OpenAI |
## Licence notes

Licensing should always be checked for the exact model and version being used. A model family can contain models with different licences or additional terms. Apache 2.0 generally permits use, modification, and redistribution, including commercial use, subject to its licence conditions.

For a real project, the exact Hugging Face model card and licence file should be checked before redistribution or commercial deployment.
## Model Selection Scenarios

### Scenario 1: 8 GB laptop, no GPU, Unit 1 agent labs

**Model:** Qwen 1.5B Q4_K_M

**Reason:** The estimator gives approximately 1.20 GB at 8K context, so it has a much lower memory requirement than larger models. It is suitable for basic agent and tool-calling experiments on limited hardware.

### Scenario 2: 24 GB GPU server, 20 students

**Model:** Qwen 8B Q4_K_M

**Reason:** The estimator gives approximately 6.42 GB at 8K context. The lower memory requirement leaves more GPU memory available for multiple users, context, and other system overhead.

### Scenario 3: Public capstone with redistribution

**Model:** IBM Granite open model under Apache 2.0

**Reason:** Apache 2.0 provides clear permissions for use, modification, and redistribution, including commercial use, subject to its licence conditions. The exact model card and licence should still be checked before publishing the project.

## Conclusion

Model size, quantization, context length, available memory, tool-calling capability, and licence terms should all be considered when selecting an open model. The memory estimator provides an initial estimate, while actual local usage can vary depending on the runtime and hardware.