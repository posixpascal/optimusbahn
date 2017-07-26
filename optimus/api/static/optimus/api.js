/**
 * Optimus JavaScript API
 */

var Optimus = function () {
    return this;
};

Optimus.prototype.initChart24hMonitoring = function () {
    var parse = function (d) {
        var res = [];
        for (var i = 0; i <= 23; i++) {
            data_set = d.results["" + i]
            res.push(data_set.total_delay);
        }
        return res;
    };

    $.get('/data/delays', function (res) {
        var today = JSON.parse(res);
        $(".monitoring24-lastupdated").html(today.started);
        $.get('/data/delays/yesterday', function (res) {
                var yesterday = JSON.parse(res);
                var dataSales = {
                    labels: [
                        '0:00', '1:00', '2:00', '3:00', '4:00', '5:00', '6:00', '7:00',
                        '8:00', '9:00', '10:00', '11:00', '12:00', '13:00', '14:00', '15:00',
                        '16:00', '17:00', '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'],
                    series: [
                        parse(today),
                        //parse(yesterday)
                    ]
                };

                var optionsSales = {
                    lineSmooth: false,
                    low: 0,
                    high: 400,
                    showArea: true,
                    height: "245px",
                    axisX: {
                        showGrid: false,
                    },
                    lineSmooth: Chartist.Interpolation.simple({
                        divisor: 3
                    }),
                    showLine: false,
                    showPoint: false,
                };

                var responsiveSales = [
                    ['screen and (max-width: 640px)', {
                        axisX: {
                            labelInterpolationFnc: function (value) {
                                return value[0];
                            }
                        }
                    }]
                ];

                Chartist.Line('#chartHours', dataSales, optionsSales, responsiveSales);
            }
        )
    });
};

Optimus.prototype.initDelayedTrains = function(){
    $.get('/data/trains', function(res) {
        var dataPreferences = {
            series: [
                [25, 30, 20, 25]
            ]
        };
        res = JSON.parse(res);
        var optionsPreferences = {
            donut: true,
            donutWidth: 40,
            startAngle: 0,
            total: res.results.total_trains,
            showLabel: false,
            axisX: {
                showGrid: false
            }
        };

        Chartist.Pie('#chartPreferences', dataPreferences, optionsPreferences);

        Chartist.Pie('#chartPreferences', {
            labels: [res.results.total_trains - res.results.delayed_trains,  res.results.delayed_trains],
            series: [res.results.total_trains - res.results.delayed_trains, res.results.delayed_trains]
        });

        $(".trains-lastupdated").html(res.started);
    });
};

Optimus.prototype.initYear = function(){
    var parseMinutes = function(r){
        var result = [];
        for (var i = 1; i <= 12; i++){
            result.push(r.results["" + i].total_delay);
        }
        return result;
    };

    var parseTrains = function(r){
        var result = [];
        for (var i = 1; i <= 12; i++){
            result.push(r.results["" + i].delayed_trains);
        }
        return result;
    };


    $.get("/data/year", function(res) {
        res = JSON.parse(res);
        var data = {
            labels: ['Jan', 'Feb', 'Mar', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'],
            series: [
                parseMinutes(res),
                parseTrains(res)
            ]
        };

        var options = {
            seriesBarDistance: 10,
            axisX: {
                showGrid: false
            },
            height: "245px"
        };

        var responsiveOptions = [
            ['screen and (max-width: 640px)', {
                seriesBarDistance: 5,
                axisX: {
                    labelInterpolationFnc: function (value) {
                        return value[0];
                    }
                }
            }]
        ];

        Chartist.Bar('#chartActivity', data, options, responsiveOptions);
        $(".year-lastupdated").html(res.started);
    });
}

Optimus.prototype.initCharts = function () {
    // 24stunden
    this.initChart24hMonitoring();
    this.initDelayedTrains();
    this.initYear();
};


window.optimus = new Optimus();