package com.hi.webapp.hipro.keyword1.apiaction;

import com.hi.framework.controller.SuperAction;
import com.hi.framework.entity.AjaxEntity;
import com.hi.webapp.hipro.keyword1.entity.proKeyword1;
import com.hi.webapp.hipro.keyword1.service.Prokeyword1Service;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.annotation.Resource;
import java.util.HashMap;
import java.util.Map;

@Controller
@RequestMapping(value = "/test/keyword1")
public class ProKeyword1Action extends SuperAction<ProKeyword1> {
    @Resource
    private ProKeyword1Service proKeyword1Service;

    @ResponseBody
    @RequestMapping(value = "/read.htm", method = RequestMethod.POST)
    public AjaxEntity read() {
        long userId = getUserId(getRequest());
        Map<String, Object> where = getAjaxUtil().getWhereMap();
        where.put("userId", userId);
        return new AjaxEntity(proKeyword1Service.read(where));
    }

    @ResponseBody
    @RequestMapping(value = "/update.htm", method = RequestMethod.POST)
    public AjaxEntity update() {
        long userId = getUserId(getRequest());
        Map<String, Object> whereMap = getAjaxUtil().getWhereMap();
        whereMap.put("userId", userId);
        return new AjaxEntity(new HashMap() {{            put("resultCount",proKeyword1Service.update(whereMap, getAjaxUtil().getUpdateMap()));
        }});    }

    @ResponseBody
    @RequestMapping(value = "/page.htm", method = RequestMethod.POST)
    public AjaxEntity page() {
        long userId = getUserId(getRequest());
        Map<String, Object> whereMap = getAjaxUtil().getWhereMap();
        whereMap.put("userId", userId);
        return new AjaxEntity(proKeyword1Service.page(whereMap, getAjaxUtil().getSortColumnMap(), getAjaxUtil().getPageIndex(), getAjaxUtil().getPageSize()));
    }


    @ResponseBody
    @RequestMapping(value = "/list.htm", method = RequestMethod.POST)
    public AjaxEntity list() {
        long userId = getUserId(getRequest());
        Map<String, Object> whereMap = getAjaxUtil().getWhereMap();
        whereMap.put("userId", userId);
        return new AjaxEntity(proKeyword1Service.list(whereMap, getAjaxUtil().getSortColumnMap()));
    }

    @ResponseBody
    @RequestMapping(value = "/delete.htm", method = RequestMethod.POST)
    public AjaxEntity delete() {
        long userId = getUserId(getRequest());
        Map<String, Object> whereMap = getAjaxUtil().getWhereMap();
        whereMap.put("userId", userId);
        return new AjaxEntity(new HashMap() {{            put("resultCount", proKeyword1Service.delete(whereMap));
        }});    }


}