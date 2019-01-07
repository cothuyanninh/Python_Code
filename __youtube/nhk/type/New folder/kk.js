$().ready(function() {
	var app        = Clip;
	var _sliderAry = [];
	var $sections  = null;
	var $more      = null;
	var $back      = null;
	var ajaxComp   = true;

	var updateSlider = function() {
		for(var i=0;i<_sliderAry.length;i++) {
			_sliderAry[i].update();
		};
	};
	var clearSlider = function() {
		for(var i=0;i<_sliderAry.length;i++) {
			_sliderAry[i].clear();
		};
	};
	var initSlider = function() {
		_sliderAry = null;
		_sliderAry = [];
		$sections = $('div#main section');

		for(var i=0; i<$sections.length; i++) {
			$section = $($sections[i]);
			var id = $section.attr('id');
			if($section) {
				var _slider = new schoolSlider('#' + id);
				_slider.init();
				_sliderAry.push(_slider);
			}
		}
	};
	var onResizeToSlider = function() {
		$(window).on('resize.slider',function() {
			updateSlider();
		});
	};
	var hideMore = function(sliderObj) {
		var $tgt    = sliderObj.$parent;
		var itemNum = $tgt.find('div.item').length;
		var result  = $tgt.find('h2').data('result');

		if(itemNum == result){
			$more.hide();
		}
	};
	var add = function() {
		var slider = _sliderAry[0];
		slider.updateAllbox();
		ajaxComp = true;
		hideMore(slider);
	};
	var detail = function() {
		var slider = _sliderAry[0];
		slider.clearSlider();
		$more = slider.initMoreBtn();
		$back = slider.initBackBtn();
		hideMore(slider);

		$more.on('click',function() {
			if (!ajaxComp) return false;
			ajaxComp = false;
			app.add($(this).parents('section'));
			return false;
		});
		$back.on('click',function() {
			$more.off();
			$back.off();
			slider.returnSlider();
			app.back();
			$('#' + selectTgtId).hide();
			return false;
		});
	};
	var eventCallback = function(status) {
		switch(status) {
			case 'init':
				initSlider();
				scrollSection();
				_language.init();
				break;
			case 'update':
				initSlider();
				detail();
				break;
			case 'add':
				add();
				break;
		}
	}

	var $fixMenu = $('div.global');
	var selectTgtId = '';
	$('#main').on('click', 'section > h2', function() {
		selectTgtId = $(this).parents('section').attr('id');
	});
	var scrollSection = function() {
		if (selectTgtId) {
			var subHi = $fixMenu.height();
			$("html,body").animate({scrollTop: $('#' + selectTgtId).offset().top - (subHi + 70)});
			selectTgtId = '';
		}
	};

	app.init(eventCallback);
	itemMenu.init(app.menuCallback);
	onResizeToSlider();


	var _schoolheader=g_schoolheader;

	var _language={
		EN_TEXT:{
			title:'Short Video'
		}
		,init:function(){
			var _this=this;
			_this.setBodyClass(_this.getCookie(),function(lang_){
				_this.changeContents(lang_)

			});

		}
		,setBodyClass:function(lang,cb){
			var body=$('body');
			if(body.hasClass(lang)){
				return;
			}
			var _LANG=schoolConfig.LANGUAGE;
			body.removeClass(_LANG.EN+' '+_LANG.JA).addClass(lang);
			cb(lang)

		}
		,changeContents:function(lang){
			var _this=this;

			if(!lang || lang=='ja'){
				return
			}
			$('#commonItems').find('h1').html('<span>'+_this.EN_TEXT.title+'</span>')
			_this.changeSliderName(lang)
			_this.changeKyokaMenu(lang)
			_this.changeGradeMenu(lang)
			$('#clip_keyword').attr({'placeholder':'keyword'})
			var sortLi=$('#commonItems').find('li.sort')
			sortLi.children('h2').html('Sort by');
			$('#sort').find('.update').html('newest to oldest').end().find('.ranking').html('popularity');
			$('#sort').children('strong').html('<span>popularity</span>')
		}
		,changeSliderName:function(lang){
			var confMenu=schoolConfig.kyoka_menu_en;
			//スライダー教科名変更
			for(var p in confMenu){
				//console.log(kyokacConf[p])
				if($('#'+p+'Slider').length){
					var span=$('#'+p+'Slider').find('h2 span')
					$('#'+p+'Slider').find('h2').html(confMenu[p]).append(span)
				}
			}
		}
		,changeKyokaMenu:function(lang){
			var confGrade=schoolConfig.kyoka_menu_en;
			$('#subject').find('strong>span').html('Subject')
			var $ul=$('#subject').find('ul').addClass('en');

			$ul.find('li').each(function(){
				for(var p in confGrade){
					if($(this).data('param')==p){
						$(this).html(confGrade[p])
						continue;
					}
				}
			})


		}
		,changeGradeMenu:function(lang){
			var confGrade=schoolConfig.grade_menu_en;
			$('#grade').find('strong>span').html('Grade')
			var $ul=$('#grade').find('ul');

			$ul.find('li').each(function(){
				for(var p in confGrade){
					if($(this).data('param')==p){
						$(this).html(confGrade[p]);
						continue;
					};
				};
			});
		}
		,getCookie:function(){
			return _schoolheader.getCookie();

		}

	}
});

var Clip = (function() {
	var slider     = '';
	var config     = schoolConfig;
	var kyokaList  = config.kyokaList;
	var notifyList = [];
	var Util       = itemUtil;
	var sliderH2ClickMore = 1;

	var fetch = function(args){
		args = Util.extend(Model.getArgs(), args);
			var url = config.api.clip;
			url += "?kyoka=" + args.kyoka;
			url += "&size="  + args.size;
			url += "&sort="  + args.sort;
			url += "&from="  + args.from;

		if(args.grade !== "all") {
			url += "&grade=" + args.grade;
		}
		if(args.kw) {
			url += "&kw=" + encodeURI(args.kw);
		}
		return $.ajax({
			type:     'get',
			dataType: 'json',
			url:      url,
			timeout:  5000
		});
	};

	var fetchAll = function() {
		var args = Util.extend(Model.getArgs(), {
			size: 20,
			from: 1,
		});

		var response = $.map(Model.getKyokaList(), function(kyoka, i)  {
			args.kyoka = kyoka;
			var res = fetch(args);
			return res;
		});

		return $.when.apply(null, response);
	};


	var Model  = {
		rawData: [],
		status:    '',
		kyoka:     'all',
		grade:     'all',
		kw:        null,
		sort:      'ranking',
		kyokaList: [],
		$menu:     null,
		$current:  null,
		$detail:   null,

		init: function() {
			this.fetchAll('init');
		},
		fetchAll: function(init) {
			_this = this;

			fetchAll().done(function() {
				var dataAll = [];
				for (var i = 0; i < arguments.length; i++) {
					var res = arguments[i][0].response;
					if(res.info.result > 0 || !init) {
						dataAll.push(res);
					}
				}
				_this.status = 'init';
				_this.setData(dataAll);
				_this.initKyokaList(dataAll);
				_this.callEvent();
			}).fail(function(err)  {
				_this.status = 'error';
				_this.callEvent();
			});
		},
		changeArgs: function() {
			_this = this;

			if(_this.kyoka === 'all') {
				_this.fetchAll();
			} else {
				fetch({
					size: 20,
					from: 1
				}).done(function(res) {
					_this.status = 'update';
					_this.setData([res.response]);
					_this.callEvent();
				}).fail(function(err)  {
					_this.status = 'error';
					_this.callEvent();
				});
			}
		},
		add: function($tgt) {
			var _this = this;
			var from  = $tgt.find('div.item').length + 1;
			_this.$detail = $tgt;

			fetch({
				size: 20,
				from: from
			}).done(function(res) {
				_this.status = 'add';
				_this.addData(res.response);
				_this.callEvent();
			}).fail(function(err)  {
				_this.status = 'error';
				_this.callEvent();
			});
		},
		addData: function(data) {
			var parsed = _this.parse(data);
			parsed.items.forEach(function(data, i)  {
				data.delay = i;
			});
			this.rawData[0].info  = parsed.info;
			this.rawData[0].items = this.rawData[0].items.concat(parsed.items);
		},
		parse: function(data) {
			var _this = this;
			var res   = {};
			res.info  = data.info;
			res.items = [];
			if(res.info.result > 0) {
				res.items = $.map(data.records, function(item) {
					item.cat = "c";
					return Util.parseItem(item);
				});
			}
			return res;
		},
		setData: function(dataAll) {
			this.rawData = $.map(dataAll, function(sectionData)  {
				return _this.parse(sectionData);
			});
		},
		getDataset:function() {
			var dataset = {};
			this.rawData.forEach(function(data)  {
				dataset[data.info.kyoka] = data;
			});
			return dataset;
		},
		initKyokaList: function(dataAll) {
			var _this = this;
			this.kyokaList = $.map(_this.rawData, function(sectionData) {
				return sectionData.info.kyoka;
			});
		},
		getKyokaList: function() {
			if(this.kyokaList.length > 0) {
				return this.kyokaList;
			} else {
				return kyokaList;
			}
		},
		setArgs: function(args) {
			if (args.kw !== undefined) {
				this.kw = args.kw;
			}
			if (args.kyoka) {
				this.kyoka = args.kyoka;
			}
			if (args.grade) {
				this.grade = args.grade;
			}
			if (args.sort) {
				this.sort = args.sort;
			}
		},
		getArgs: function() {
			return {
				kyoka: this.kyoka,
				grade: this.grade,
				kw:    this.kw,
				sort:  this.sort
			};
		},
		callEvent: function() {
			Event.action(this.status);
		},
	};

	var View = {
		templates: {
			section: {
				wrap:   '<section id="" class="largeSlider"></div>',
				head:   '<h2 data-result="{{result}}" data-kyoka="{{kyoka}}">{{kyokaStr}}<span>{{resultStr}}</span></h2>',
				slider: '<div class="sliderInner"><div class="sliderNavi prev" /><div class="sliderNavi next" /><div class="items"></div></div>',
			},
			item: {
				wrap:      '<div class="{{baseClass}}"><a href="{{href}}"></a></div>',
				image:     '<div class="image"><img width="182" height="101" alt="" src="{{src}}"></div>',
				details:   '<div class="details"><div class="subject">{{kyokaStr}}</div><div class="head"><p class="grade">{{gradeStr}}</p><div class="title">{{title}}</div><div class="text">{{text}}</div></div><div class="time">{{time}}</div>',
			}
		},
		init: function() {
			if(this.$main == null) {this.$main = $('#main');}
			this.$main.empty();
		},
		isNoMovie: function(data) {
			return data.movieFlag < 2 ? false : true;
		},
		renderError: function() {
			this.init();
			this.$main.html(Util.getErrorHtml('ready'));
		},
		renderAdd: function() {
			var _this    = this;
			var dataAll  = Model.getDataset();
			var key      = Object.keys(dataAll);
			var $tgt     = Model.$detail;
			var htmlList = [];

			if (dataAll[key]) {
				var items    = dataAll[key].items;
				var from     = dataAll[key].info.from - 1;
				for(var i = from; i < items.length; i++) {
					htmlList.push(_this.itemHtml(items[i]));
				}
			}
			$tgt.find('div.items').append($(htmlList.join('')));
		},
		renderSections: function() {
			var _this   = this;
			var tmpl    = _this.templates.section;
			var dataAll = Model.getDataset();
			if(!dataAll) {
				_this.renderError();
				return;
			}

			var kyokaHtmlList = $.map(Model.getKyokaList(), function(kyoka, i)  {
				var data = dataAll[kyoka];
				if (data) {
					var kyokaStr = config.kyoka[kyoka] || '';

					/*201803*/
					var isEn = $('body').hasClass('en');
					if(isEn){
						kyokaStr=config.kyoka_menu_en[kyoka] || '';
					}
					/*201803*/

					var $wrap    = $('<div>');
					$wrap.html(tmpl.wrap);

					var $section = $wrap.find('section');
					$section.attr({'id': kyoka + 'Slider'})

					var head = _this.replaceTemplateForObject({
						kyoka:      kyoka,
						kyokaStr:   kyokaStr,
						resultStr:  '（' + data.info.result + '）',
						result:     data.info.result
					}, tmpl.head);
					$section.append($(head));

					if (data.info.result > 0) {
						$section.append($(tmpl.slider));
						$section.find('.items').html(_this.sectionItemHtml(data).join(''));
						if (data.info.result >= sliderH2ClickMore) {
							$section.addClass('openSlider');
						}
					} else {
						var notMsg=config.message.result0;
						if(isEn){
							notMsg='Not Found'
						}
						$section.append($('<p>' + notMsg + '</p>'));
						$section.attr({'class': 'noSlider'});
					}

					return $wrap.html();
				}
			});
			var html = kyokaHtmlList.join('');
			_this.$main.html(html);
		},
		sectionItemHtml: function(data) {
			var _this = this;
			var htmlList = [];
			var state = Model.getArgs();

			htmlList = data.items.map(function(item, i)  {
				return _this.itemHtml(item);
			});

			return htmlList;
		},
		itemHtml: function(data) {
			var _this      = this;
			var d          = data;
			var tmpl       = _this.templates.item;
			var appendHtml = '';
			var itemObj    = {};

			var baseClass = ["item", d.kyokaClass];
			if(d.cat === "b") {
				baseClass.push("pg");
				baseClass.push("program");
				if(this.isNoMovie(d)) {
					baseClass.push("nomovie");
				}
			} else if (d.cat === "c") {
				baseClass.push("clip");
			}

			d.baseClass = baseClass.join(' ');

			//放送日（番組）||動画時間（クリップ）
			if(!d.movieFlag && d.duration){
				d.time = d.duration;
			}

			if(d.cat === "b" && d.movieFlag === 2){
				//この回は動画を配信していません
				d.image = '/school/parts2015/common/img/img_haishinsitenai.jpg';
			}
			else if(data.cat === "b" && data.movieFlag === 3){
				//動画配信の準備中です
				d.image = '/school/parts2015/common/img/img_junibichu.jpg';
			}

			// insert DOM
			var $item = $('<div>').html(_this.replaceTemplateForObject({
				baseClass: d.baseClass,
				href:      d.url
			}, tmpl.wrap));

			var imageHtml = _this.replaceTemplate('src', tmpl.image, d.image);
			itemObj = Util.extend(itemObj, {
				title:    d.title,
				text:     d.text,
				time:     d.time,
				kyokaStr: d.kyokaName,
				gradeStr: d.gakunen,
			});
			var detailHtml = _this.replaceTemplateForObject(itemObj, tmpl.details);
			$item.find('a').html(imageHtml);
			$item.find('a').append($(detailHtml));

			return $item.html();
		},
		replaceTemplateForObject: function(obj, templateStr) {
			var str = templateStr;
			for(var key in obj) {
				str = this.replaceTemplate(key, str, obj[key]);
			}
			return str;
		},
		replaceTemplate: function(key, templateStr, replaceStr) {
			if(!key) return '';
			return templateStr.replace(new RegExp('{{' + key + '}}', 'g'), replaceStr);
		},
	};

	var Event = {
		init: function() {
			this.on();
		},
		callback: function($this) {
			var $parent = $this.parent().parent();
			var _this   = this;
			_this.changeMenu($parent.attr('id'), $this.data('param'));
		},
		action: function(status) {
			switch(status) {
				case 'init':
					View.renderSections();
					this.notify(status);
					break;
				case 'update':
					View.renderSections();
					this.notify(status);
					break;
				case 'error':
					View.renderError();
					break;
				case 'add':
					View.renderAdd();
					this.notify(status);
					break;
			}
		},
		notify: function(obj) {
			var argsObj = obj;
			for(var i = 0; i < notifyList.length; i++) {
				notifyList[i](argsObj);
			}
		},
		on: function() {
			var _this = this;
			$('#clip_search').on('click', function() {
				_this.changeMenu('keyword', $('#clip_keyword').val());
			});

			$('#main').on('click', 'section > h2', function() {
				var $this = $(this);
				if ($this.data('result') < sliderH2ClickMore) {return false;}
				if ($this.parents('section').hasClass('opened')) {return false;}
					$('#subject').find('li.' + $this.data('kyoka')).click();
					$('body,html').animate({
						scrollTop: 0
					}, 0);
			});

			var $main = $('#main');
			$main.on('mouseenter', 'div.item', function(e) {
				var href = $(this).find('a').attr('href');
				Util.fancybox($(this), href);
				e.preventDefault();
			});
		},
		changeMenu: function(tgtId, param) {
			if (!tgtId) {return false;}
			$('#' + tgtId).data({'selected': param});
			var args = {};
			switch(tgtId) {
				case 'subject':
					args.kyoka = param;
					break;
				case 'grade':
					args.grade = param;
					break;
				case 'sort':
					args.sort = param;
					break;
				case 'keyword':
					args.kw = param;
					break;
			}

			Model.setArgs(args);
			Model.changeArgs();
		},
	}

	var init = function(cb) {
		notifyList.push(cb)
		View.init();
		Model.init();
		Event.init();
	};
	var add = function($this) {
		Model.add($this);
	}
	var back = function() {
		$('#subject').find('li.subject_all').click();
	}
	var menuCallback = function($this) {
		Event.callback($this);
	};

	var modules = {
		init: init,
		add:   add,
		back:  back,
		menuCallback: menuCallback,
	}

	return modules;
})();
