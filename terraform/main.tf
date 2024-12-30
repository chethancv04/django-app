provider "kubernetes" {
  config_path = "C:\\Users\\chethan\\.kube\\config"
}

resource "kubernetes_namespace" "django" {
  metadata {
    name = "django"
  }
}

resource "kubernetes_deployment" "django-app" {
  metadata {
    name      = "django-app"
    namespace = kubernetes_namespace.django.metadata[0].name
  }

  spec {
    replicas = 2

    selector {
      match_labels = {
        app = "django-app"
      }
    }

    template {
      metadata {
        labels = {
          app = "django-app"
        }
      }

      spec {
        container {
          name  = "django-container"
          image = "chethancv28/far_pro:latest"

          port {
            container_port = 8000
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "django-service" {
  metadata {
    name      = "django-service"
    namespace = kubernetes_namespace.django.metadata[0].name
  }

  spec {
    selector = {
      app = kubernetes_deployment.django-app.spec[0].template[0].metadata[0].labels.app
    }

    port {
      port        = 8000
      target_port = 8000
    }

    type = "NodePort"
  }
}
