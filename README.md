# gRPC Server for GPT4Free Integration

This server provides the capabilities of the [gpt4free](https://github.com/xtekky/gpt4free) library, including image and text generation through various models.

## Structure

- **`./protos/ai.proto`** — the definition of the gRPC API.
- **`./config/`** — directory containing configuration files that can be customized to manage the gRPC service.

## How to Run

1. Set the environment variable `CONFIG_PATH` pointing to the configuration file in YAML format (e.g., `config/dev.cfg.yaml`):
    - For Linux/macOS:
      ```bash
      export CONFIG_PATH=./config/dev.cfg.yaml
      ```
    - For Windows:
      ```bash
      set CONFIG_PATH=./config/dev.cfg.yaml
      ```

2. Start the server:
    ```bash
    python ai.py
    ```

3. Your server will now be available for gRPC requests supporting image and text generation.

## Configuration

All settings for configuring the gRPC service are located in the configuration file specified by the `CONFIG_PATH` environment variable. You can modify these settings to work with different models and generation features.
Make sure to set the `sys_promt_path` in your YAML configuration. This path points to the file containing the chatbot's system prompt. If this setting is omitted or the file is missing, the prompt will not be loaded and will remain empty.

## Important!

- For the server to run successfully, the `CONFIG_PATH` environment variable must be set and point to an existing configuration file.
- The default configuration file does not exist and must be created manually.

## gRPC API Methods

<details>
  <summary>Available Methods Description</summary>

### 1. `GetSuggest`
Generates text suggestions based on the given input.

- **Input:** User ID and a text prompt.  
- **Output:** A response indicating whether the request was successful and the generated suggestion.  

---

### 2. `ClearHistory`
Clears the interaction history for a specific user.

- **Input:** User ID.  
- **Output:** A confirmation of whether the history was successfully cleared.  

---

### 3. `GetInformation`
Retrieves details about the current models in use.

- **Input:** No parameters required.  
- **Output:** Information about the active chat and image generation models.  

---

### 4. `ChangeModel`
Switches the model used for text or image generation.

- **Input:** The model type (text or image) and the desired model name.  
- **Output:** A success status and a message indicating whether the switch was successful.  

---

### 5. `GenerateImage`
Creates an image based on the given text prompt.

- **Input:** User ID and a text prompt describing the desired image.  
- **Output:** A URL linking to the generated image.  

</details>
