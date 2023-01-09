
        $(document).ready(function() {
            $('#id_{{ name }}').fileinput({
                showCaption: false,
                showPreview: false,
                showRemove: false,
                showUpload: false,
                browseOnZoneClick: true,
                language: 'es',
                allowedFileTypes: ['image'],
                browseClass: 'btn btn-primary btn-block',
                browseLabel: 'Examinar',
                browseIcon: '<i class="glyphicon glyphicon-folder-open"></i> ',
                removeClass: 'btn btn-danger',
                removeLabel: 'Eliminar',
                removeIcon: '<i class="glyphicon glyphicon-trash"></i> ',
            });
        });
