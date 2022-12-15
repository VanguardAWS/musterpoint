let imperialKnightsUnits = new Vue({
    el: '#api',
    delimiters: ['[[', ']]'], // This is new
    data: {
    imperialKnightsUnitsList: [],
    imperialKnightsWargearList: [],
    armyList: [],
    pointTotal: 0,
    finalPointTotal: null,
    completedArmyList: null,
    listComplete: false
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
    addUnit: function(unit) {
        this.pointTotal = unit.point_value + this.pointTotal
        unitCopy = JSON.parse(JSON.stringify(unit))
        this.armyList.push(unitCopy)
    },
    removeUnit: function(index){
        let currentUnit = this.armyList[index]
        this.pointTotal = this.pointTotal - currentUnit.point_value
        this.armyList.splice(index, 1)
    },
    addWeapon: function(unit, weapon, wargear, weaponindex) {
        this.pointTotal = wargear.point_value + this.pointTotal
        unit.point_value = unit.point_value + wargear.point_value
        unit.wargear.push(weapon)
        unit.optional_wargear.splice(weaponindex, 0) 
    },
    removeWeapon: function(unit, index, wargear, wargearindex) {
        this.pointTotal = this.pointTotal - wargear.point_value
        unit.point_value = unit.point_value - wargear.point_value
        this.armyList[index].wargear.splice(wargearindex, 1)
    },
    finishList: function(){
        this.completedArmyList = this.armyList
        this.finalPointTotal = this.pointTotal
        this.armyList = null
        this.pointTotal = null
        this.listComplete = true
    },
    editList: function(){
        this.armyList = this.completedArmyList
        this.pointTotal = this.finalPointTotal
        this.completedArmyList = null
        this.finalPointTotal = null
        this.listComplete = false
    }
    },
    beforeMount: function() {
        this.getImperialKnightsWargear(),
        this.getImperialKnightsUnits()
    }
});
