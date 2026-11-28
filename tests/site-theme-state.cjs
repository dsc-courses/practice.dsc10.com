const fs=require('fs'),vm=require('vm'),assert=require('assert/strict');
const source=fs.readFileSync('assets/site-theme.js','utf8');
function boot(store=new Map(),blocked=false){
 const listeners={},events={};
 const buttons=['light','dark'].map(theme=>({dataset:{themeChoice:theme},setAttribute(k,v){this[k]=v;},closest(){return this;}}));
 const root={dataset:{}};
 vm.runInNewContext(source,{document:{documentElement:root,querySelectorAll:()=>buttons,addEventListener:(k,f)=>listeners[k]=f},window:{addEventListener:(k,f)=>events[k]=f},localStorage:{getItem(k){if(blocked)throw Error('blocked');return store.get(k)??null},setItem(k,v){if(blocked)throw Error('blocked');store.set(k,v)}}});
 return {root,buttons,click:i=>listeners.click({target:buttons[i]}),ready:()=>listeners.DOMContentLoaded(),storage:events.storage};
}
let store=new Map(),home=boot(store);assert.equal(home.root.dataset.siteTheme,'light');
home.click(1);assert.equal(home.root.dataset.siteTheme,'dark');home.ready();assert.equal(home.buttons[1]['aria-pressed'],'true');
let quiz=boot(store);quiz.ready();assert.equal(quiz.root.dataset.siteTheme,'dark');
quiz.click(0);assert.equal(boot(store).root.dataset.siteTheme,'light');
home.storage({key:'dsc10-theme',newValue:'light'});assert.equal(home.root.dataset.siteTheme,'light');
home.storage({key:'pt-done',newValue:'dark'});assert.equal(home.root.dataset.siteTheme,'light');
assert.equal(boot(new Map([['dsc10-fa26-quiz2-theme','dark']])).root.dataset.siteTheme,'dark');
let noStorage=boot(new Map(),true);noStorage.click(1);assert.equal(noStorage.root.dataset.siteTheme,'dark');
console.log('PASS: light default, early toggle, cross-page persistence, cross-tab synchronization, independent progress keys, prototype migration, blocked-storage fallback.');
