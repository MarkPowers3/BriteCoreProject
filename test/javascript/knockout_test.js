/* knockout.js */

    var vm;

    $(function() {

        ko.bindingHandlers.numeric = {
            init: function (element, valueAccessor) {
                $(element).on("keydown", function (event) {
                    // Allow: backspace, delete, tab, escape, and enter
                    if (event.keyCode == 46 || event.keyCode == 8 || event.keyCode == 9 || event.keyCode == 27 || event.keyCode == 13 ||
                        // Allow: Ctrl+A
                        (event.keyCode == 65 && event.ctrlKey === true) ||
                        // Allow: . ,
                        (event.keyCode == 188 || event.keyCode == 190 || event.keyCode == 110) ||
                        // Allow: home, end, left, right
                        (event.keyCode >= 35 && event.keyCode <= 39)) {

                        return;
                    }
                    else {
                        // Ensure that it is a number and stop the keypress
                        if (event.shiftKey || (event.keyCode < 48 || event.keyCode > 57) && (event.keyCode < 96 || event.keyCode > 105)) {
                            event.preventDefault();
                        }
                    }
                });
            }
        };

        ko.bindingHandlers.currency = {
            init: function(element, valueAccessor) {
                $(element).on("blur", function (event) {
                    var val = $(element).val();
                    if (val.length > 0) {
                        $(element).val("$" + val.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,"));
                    }
                });

                $(element).on("focus", function (event) {
                    var val = $(element).val();
                    $(element).val(val.replace(/[\$]/, '').replace(/\,/g,''));
                });
            }
        };

        function RiskViewModel() {
            var self = this;
            self.risks = ko.observableArray([{ 'id': '', 'name': 'Select One...' }]);
            self.fields = ko.observableArray([]);

            self.init = function() {
                self.getRisks()
            };

            self.addRisk = function(risks) {
                self.risks.push(risks);
            };

            self.addField = function(field) {
                self.fields.push(field);
                if (field.type == 'date') {
                    $( "#" + field.uniqueId ).datepicker();
                }
            };

            self.showFields = ko.observable(false);

            self.enableFields = function(option, event) {
                var id = $('#' + event.currentTarget.id).val();
                self.getRisk(id);
                self.showFields(show = id.length == 0 ? false : true);
            };

            self.maxLength = function(field) {
                length = typeof field.maxLength === 'undefined' ? 100 : field.maxLength;
                return length;
            };

            this.getRisk = function(id) {
                if (id.length == 0)
                    return;

                $.getJSON("http://127.0.0.1:5000/risk/" + id, function(data) {
                    vm.fields.removeAll();
                    $.each(data.fields, function(index, value) {
                        vm.addField(value);
                    });
                });
            };

            this.getRisks = function() {
                $.getJSON("http://127.0.0.1:5000/risks", function(data) {
                    $.each(data, function(index, value) {
                        vm.addRisk(value);
                    });
                });
            }
        }

        vm = new RiskViewModel();
        vm.init();

        ko.applyBindings( vm );


    });


