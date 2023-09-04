terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.69.0"
    }
  }
}

provider "azurerm" {
  skip_provider_registration = true # This is only required when the User, Service Principal, or Identity running Terraform lacks the permissions to register Azure Resource Providers.
  features {}
}

resource "azurerm_resource_group" "enigma-service-rg" {
  name     = "enigma-service-resource-group"
  location = "East US"
  tags = {
    environment = "dev"
  }
}

resource "azurerm_container_registry" "enigma-acr" {
  name                = "enigmaContainerRegistry"
  resource_group_name = azurerm_resource_group.enigma-service-rg.name
  location            = azurerm_resource_group.enigma-service-rg.location
  sku                 = "Basic"
  admin_enabled       = true
}

resource "azurerm_service_plan" "enigma-service-sp" {
  name                = "enigma-service-plan"
  resource_group_name = azurerm_resource_group.enigma-service-rg.name
  location            = azurerm_resource_group.enigma-service-rg.location
  os_type             = "Linux"
  sku_name            = "F1"
}


resource "azurerm_linux_web_app" "enigma-service" {
  name                = "enigma-service"
  resource_group_name = azurerm_resource_group.enigma-service-rg.name
  location            = azurerm_service_plan.enigma-service-sp.location
  service_plan_id     = azurerm_service_plan.enigma-service-sp.id

  site_config {}
}