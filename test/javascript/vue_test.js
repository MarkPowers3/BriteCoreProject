/* vue_test.js */

    var risks;

    function numberEventListener(event) {
        el = event.currentTarget;
        let regex = /^[0-9]*$/;
        if (!regex.test(el.value)) {
            el.value = el.value.slice(0, -1)
        }
    }

    function currencyEventListener(event) {
        el = event.currentTarget;
        if (event.type == 'blur') {
            if (el.value.length > 0) {
                el.value = "$" + el.value.replace(/(\d)(?=(\d{3})+(?!\d))/g, "$1,");
            }
        }
        else if (event.type == 'focus') {
            el.value = el.value.replace(/[\$]/, '').replace(/\,/g,'');
        }
    }

    Vue.component('date-picker', {
        template: '<input/>',
        mounted: function() {
            $(this.$el).datepicker();
        },
        beforeDestroy: function() {
            $(this.$el).datepicker('hide').datepicker('destroy');
        }
    });

    Vue.directive('number', {
        bind(el) {
            el.addEventListener('keyup', numberEventListener);
        },
        unbind(el) {
            el.removeEventListener('keyup', numberEventListener);
        }
    });

    Vue.directive('currency', {
        bind(el) {
            el.addEventListener('blur', currencyEventListener),
            el.addEventListener('focus', currencyEventListener)
        },
        unbind(el) {
            el.removeEventListener('blur', currencyEventListener);
            el.removeEventListener('focus', currencyEventListener);
        }
    });

    $(function() {

        risks = new Vue({
            el: '#app-risks',
            data: {
                title: 'Risk Test Page',
                base_url: "http://127.0.0.1:5000",
                risks: [{ 'id': '', 'name': 'Select One...' }],
                fields: [],
                showFields: false
            },
            mounted() {
                 this.init();
            },
            updated() {
                $('.col-md-10 input').val("");
            },
            methods: {
                init: function() {
                    this.getRisks();
                },
                enableFields: function (event) {
                    var id = $('#' + event.currentTarget.id).val();
                    this.getRisk(id);
                    this.showFields = id.length == 0 ? false : true;
                },
                addRisk: function(risk) {
                    this.risks.push(risk);
                },
                addField: function(field) {
                    this.fields.push(field);
                },
                maxLength: function(field) {
                   var length = typeof field.maxLength === 'undefined' ? 100 : field.maxLength;
                   return length;
                },
                getRisk: function(id) {
                    if (id.length == 0)
                        return;

                    $.getJSON(this.base_url + "/risk/" + id, function(data) {
                        risks.fields = [];
                        $.each(data.fields, function(index, value) {
                            risks.addField(value);
                        });
                    });
                },
                getRisks: function() {
                    $.getJSON(this.base_url + "/risks", function(data) {
                        $.each(data, function(index, value) {
                            risks.addRisk(value);
                        });
                    });
                }
            }
        });

    });