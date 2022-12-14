let imperialKnightsUnits = new Vue({
    el: '#api',
    delimiters: ['[[', ']]'], // This is new
    data: {
    imperialKnightsUnitsList: [],
    imperialKnightsWargearList: [],
    armyList: [],
    pointTotal: 0,
    },
    methods: {
    getImperialKnightsUnits: function() {
        axios({
            method: 'GET',
            url: '/api/units/',
            
        }).then(res => this.imperialKnightsUnitsList = res.data)
    },
    getImperialKnightsWargear: function() {
        axios({
            method: 'GET',
            url: '/api/wargear/',
            
        }).then(res => this.imperialKnightsWargearList = res.data)
    },       
    addUnit: function(index) {
        let currentUnit = this.imperialKnightsUnitsList[index]
        this.pointTotal = currentUnit.point_value + this.pointTotal
        this.armyList.push(currentUnit)
    },
    removeUnit: function(unit){
        let currentUnit = this.imperialKnightsUnitsList
        this.armyList.splice(currentUnit, 1)
    }
    },
    beforeMount: function() {
        this.getImperialKnightsWargear(),
        this.getImperialKnightsUnits()
    }
});
