let imperialKnightsUnits = new Vue({
    el: '#api',
    delimiters: ['[[', ']]'], // This is new
    data: {
    imperialKnightsUnitsList: [],
    imperialKnightsWargearList: [],
    armyList: [],
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
    addUnit: function() {
        let currentUnit = this.imperialKnightsUnitsList
        this.armyList.push(currentUnit[0])
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


