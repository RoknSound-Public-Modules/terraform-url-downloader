data "external" "download" {
  program = ["python", "${path.module}/download.py"]

  query = {
    # arbitrary map from strings to strings, passed
    # to the external program as the data query.
    url         = var.url
    output_path = var.output_path
  }
}

resource "null_resource" "cleanup" {
  count = var.cleanup && var.output_path != null ? 1 : 0
  provisioner "local-exec" {
    command = "rm ${element(data.local_file.file, count.index)}"
  }
}

data "local_file" "file" {
  count    = var.output_path != null ? 1 : 0
  filename = data.external.download.result.output_path
}
