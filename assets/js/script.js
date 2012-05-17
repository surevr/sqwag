var SQ = {
  init: function(context) {
    var self = this;
    self.backbone = context.backbone;
    self.bindLinks();  
    self.bindForms(); 
    self.bindButtons();
    self.bindSqwags();
    // initialize backbone
    self.backbone.init(context);
    self.router = context.router;
    //initialize routers 
    self.router.init();
    // route to a template
    self.router.routeTo(context.route);
  },

  fetchFeed: function() {
    $('#feed').click();
  },
  
  close: function() {
    $('.close').click();
  },
  
  notify: function(data) {
    $('#console').text(data).fadeIn('slow');
  },
  
  refresh: function() {
    window.location.reload();
  },
  
  bindLinks: function() {
    var self = this;
    $('.js-load').click(function() {
      var route = $(this).attr('href').replace('#','');
      self.router.routeTo(route);
      return false;
    });

    $('.js-link').click(function() {
      var link = $(this).attr('href');
      var jxhr = $.get(link).complete(function() {
        self.refresh();
      });
      return false;
    });
  },
  
  bindForms: function() {
     var self = this;
     $('#login-form form').ajaxForm({
      dataType: 'json',
      success: function(data) {
        if(data.status == 1) {
          self.refresh();
        }
        else {
          self.notify(data.error);
          self.close(); // TODO : refactor
        }
      }
    }); 
    
    $('#register-form form').ajaxForm({
      dataType: 'json',
      success: function(data) {
        if(data.status == 1) {
          self.notify(data.status);
        }
        else {
          self.notify(data.error);
        }
        self.close();
      }
    });
  },
  bindButtons: function() {
    var self = this;
    $('.resqwag').live('click', function() {
      var square_id = $(this).data('id');
      $.post('/api/square/share', {'square_id' : square_id}, function() {
        self.notify('ho gaya!');
        self.fetchFeed();
      });
    });
  },
  bindSqwags: function() {
    $('.sqwag').live('mouseover mouseout', function(event) {
      var mask = $(this).find('.mask');
      if(event.type == 'mouseover') {
        mask.show();
      }
      else {
        mask.hide();
      }
    });
  }
}